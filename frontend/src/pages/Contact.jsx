import { useState } from 'react'
import { useLang, t } from '../context/LangContext'
import { useInView } from 'react-intersection-observer'
import { sendContact } from '../api/api'

function Fade({ children, delay=0, style={} }) {
  const { ref, inView } = useInView({ threshold:0.1, triggerOnce:true })
  return (
    <div ref={ref} style={{ opacity:inView?1:0, transform:inView?'translateY(0)':'translateY(28px)', transition:`opacity 0.65s ease ${delay}s, transform 0.65s ease ${delay}s`, ...style }}>
      {children}
    </div>
  )
}

function InfoCard({ icon, label, value, href }) {
  const inner = (
    <div style={{ display:'flex', alignItems:'flex-start', gap:'1.2rem', padding:'1.5rem 2rem', background:'white', borderRadius:16, boxShadow:'0 4px 20px rgba(12,25,49,0.06)', transition:'all 0.3s' }}
      onMouseEnter={e => { e.currentTarget.style.transform='translateY(-3px)'; e.currentTarget.style.boxShadow='0 12px 32px rgba(12,25,49,0.12)' }}
      onMouseLeave={e => { e.currentTarget.style.transform='none'; e.currentTarget.style.boxShadow='0 4px 20px rgba(12,25,49,0.06)' }}>
      <div style={{ width:44, height:44, borderRadius:12, background:'linear-gradient(135deg,var(--navy),var(--blue))', display:'flex', alignItems:'center', justifyContent:'center', color:'var(--gold)', fontSize:'1rem', flexShrink:0 }}>
        <i className={icon} />
      </div>
      <div>
        <div style={{ fontSize:'0.75rem', fontWeight:700, letterSpacing:'0.1em', textTransform:'uppercase', color:'var(--gray)', marginBottom:'0.3rem' }}>{label}</div>
        <div style={{ fontSize:'0.95rem', fontWeight:600, color:'var(--navy)' }}>{value}</div>
      </div>
    </div>
  )
  return href ? <a href={href} style={{ textDecoration:'none' }}>{inner}</a> : inner
}

function InputField({ label, type='text', value, onChange, error, textarea=false, required=false }) {
  const [focused, setFocused] = useState(false)
  const baseStyle = {
    width:'100%', padding:'0.75rem 1rem',
    border:`1.5px solid ${error?'#EF4444':focused?'var(--green)':'rgba(10,25,60,0.15)'}`,
    borderRadius:10, fontSize:'0.92rem',
    fontFamily:"'Outfit',sans-serif",
    background:'white', color:'var(--navy)', outline:'none',
    transition:'border-color 0.25s, box-shadow 0.25s',
    boxShadow: focused ? `0 0 0 3px ${error?'rgba(239,68,68,0.15)':'rgba(106,171,46,0.15)'}` : 'none',
    resize: textarea ? 'vertical' : 'none'
  }
  return (
    <div>
      <label style={{ display:'block', fontSize:'0.8rem', fontWeight:700, letterSpacing:'0.05em', textTransform:'uppercase', color:'var(--navy)', marginBottom:'0.45rem' }}>
        {label}
      </label>
      {textarea
        ? <textarea rows={5} value={value} onChange={onChange} onFocus={() => setFocused(true)} onBlur={() => setFocused(false)} style={baseStyle} />
        : <input type={type} value={value} onChange={onChange} onFocus={() => setFocused(true)} onBlur={() => setFocused(false)} style={baseStyle} />
      }
      {error && <p style={{ fontSize:'0.78rem', color:'#EF4444', marginTop:'0.3rem' }}>{error}</p>}
    </div>
  )
}

export default function Contact({ settings }) {
  const { lang, ui } = useLang()
  const addr = settings[`address_${lang}`] || settings.address_fr || "Agence Internationale"

  const [form, setForm] = useState({ name:'', email:'', phone:'', company:'', service:'', message:'' })
  const [errors, setErrors] = useState({})
  const [status, setStatus] = useState('idle') // idle | loading | success | error

  const set = (k) => (e) => setForm(f => ({ ...f, [k]: e.target.value }))

  const validate = () => {
    const errs = {}
    if (!form.name.trim())    errs.name    = ui.form_err_name
    if (!form.email.includes('@')) errs.email = ui.form_err_email
    if (!form.phone.trim())   errs.phone   = ui.form_err_phone
    if (!form.message.trim()) errs.message = ui.form_err_message
    return errs
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const errs = validate()
    if (Object.keys(errs).length) { setErrors(errs); return }
    setErrors({})
    setStatus('loading')
    try {
      await sendContact({ ...form, lang })
      setStatus('success')
      setForm({ name:'', email:'', phone:'', company:'', service:'', message:'' })
    } catch {
      setStatus('error')
    }
  }

  return (
    <>
      {/* Header */}
      <section style={{ background:'var(--navy)', padding:'5rem 3rem 4rem', position:'relative', overflow:'hidden' }}>
        <div style={{ position:'absolute', top:0, right:0, width:'40%', height:'100%', background:'var(--navy2)', clipPath:'polygon(15% 0,100% 0,100% 100%,0 100%)', opacity:0.5 }} />
        <div style={{ position:'relative', zIndex:2, maxWidth:1440, margin:'0 auto' }}>
          <p style={{ fontSize:'0.78rem', fontWeight:700, letterSpacing:'0.18em', textTransform:'uppercase', color:'var(--green)', marginBottom:'1rem' }}>
            {lang==='fr'?'— Parlons de votre projet':lang==='en'?"— Let's talk about your project":'— لنتحدث عن مشروعك'}
          </p>
          <h1 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'clamp(2.8rem,4vw,5.5rem)', fontWeight:700, lineHeight:1.05, color:'white', maxWidth:700 }}>
            {lang==='fr'?'Prêt à passer au niveau supérieur ?':lang==='en'?'Ready to reach the next level?':'هل أنت مستعد للوصول إلى المستوى التالي؟'}
          </h1>
          <p style={{ fontSize:'1rem', color:'rgba(255,255,255,0.55)', marginTop:'1rem' }}>
            {lang==='fr'?'Consultation gratuite en 48h. Nos experts vous répondent rapidement.'
            :lang==='en'?'Free consultation within 48h. Our experts respond quickly.'
            :'استشارة مجانية خلال 48 ساعة. خبراؤنا يردون بسرعة.'}
          </p>
        </div>
      </section>

      {/* Content */}
      <section style={{ background:'var(--cream)', padding:'6rem 3rem' }}>
        <div className="responsive-grid-contact" style={{ maxWidth:1440, margin:'0 auto' }}>

          {/* Left — infos */}
          <div>
            <Fade style={{ marginBottom:'3rem' }}>
              <h2 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'2rem', fontWeight:700, color:'var(--navy)', marginBottom:'0.8rem' }}>
                {lang==='fr'?'Nos coordonnées':lang==='en'?'Our Contact Details':'معلومات التواصل'}
              </h2>
              <p style={{ color:'var(--gray)', lineHeight:1.7 }}>
                {lang==='fr'?"Nous sommes disponibles du lundi au vendredi, de 8h à 18h."
                :lang==='en'?"We're available Monday to Friday, 8am to 6pm."
                :"نحن متاحون من الاثنين إلى الجمعة، من 8 صباحًا حتى 6 مساءً."}
              </p>
            </Fade>
            <div style={{ display:'flex', flexDirection:'column', gap:'1rem' }}>
              {addr && <Fade delay={0.1}><InfoCard icon="fas fa-map-marker-alt" label={ui.addr_label} value={addr} /></Fade>}
              {settings.phone && <Fade delay={0.2}><InfoCard icon="fas fa-phone" label={ui.phone_label} value={settings.phone} href={`tel:${settings.phone}`} /></Fade>}
              {settings.email && <Fade delay={0.3}><InfoCard icon="fas fa-envelope" label="Email" value={settings.email} href={`mailto:${settings.email}`} /></Fade>}
            </div>

            {/* Social */}
            <Fade delay={0.4} style={{ marginTop:'2.5rem' }}>
              <p style={{ fontSize:'0.8rem', fontWeight:700, letterSpacing:'0.1em', textTransform:'uppercase', color:'var(--gray)', marginBottom:'1rem' }}>
                {lang==='fr'?'Suivez-nous':lang==='en'?'Follow Us':'تابعونا'}
              </p>
              <div style={{ display:'flex', gap:'0.75rem' }}>
                {settings.facebook  && <SocBtn href={settings.facebook}  icon="fab fa-facebook-f" />}
                {settings.linkedin  && <SocBtn href={settings.linkedin}  icon="fab fa-linkedin-in" />}
                {settings.instagram && <SocBtn href={settings.instagram} icon="fab fa-instagram" />}
                {settings.twitter   && <SocBtn href={settings.twitter}   icon="fab fa-x-twitter" />}
              </div>
            </Fade>
          </div>

          {/* Right — form */}
          <Fade delay={0.15}>
            <div style={{ background:'white', borderRadius:24, padding:'3rem', boxShadow:'0 8px 40px rgba(12,25,49,0.08)' }}>
              {status === 'success' ? (
                <div style={{ textAlign:'center', padding:'3rem 1rem' }}>
                  <div style={{ width:72, height:72, borderRadius:'50%', background:'linear-gradient(135deg,var(--green),var(--green2))', display:'flex', alignItems:'center', justifyContent:'center', margin:'0 auto 1.5rem', boxShadow:'0 12px 32px rgba(106,171,46,0.35)' }}>
                    <i className="fas fa-check" style={{ color:'white', fontSize:'1.8rem' }} />
                  </div>
                  <h3 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'1.8rem', fontWeight:700, color:'var(--navy)', marginBottom:'0.8rem' }}>
                    {lang==='fr'?'Message envoyé !':lang==='en'?'Message Sent!':'تم إرسال الرسالة!'}
                  </h3>
                  <p style={{ color:'var(--gray)', lineHeight:1.7, marginBottom:'2rem' }}>
                    {lang==='fr'?'Nous vous répondrons dans les 48h.':lang==='en'?"We'll reply within 48 hours.":'سنرد عليك خلال 48 ساعة.'}
                  </p>
                  <button onClick={() => setStatus('idle')} className="btn-navy" style={{ margin:'0 auto' }}>
                    {lang==='fr'?'Nouveau message':lang==='en'?'New message':'رسالة جديدة'}
                  </button>
                </div>
              ) : (
                <form onSubmit={handleSubmit} noValidate>
                  <h3 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'1.6rem', fontWeight:700, color:'var(--navy)', marginBottom:'2rem' }}>
                    {lang==='fr'?'Envoyez-nous un message':lang==='en'?'Send Us a Message':'أرسل لنا رسالة'}
                  </h3>
                  <div className="responsive-grid-2" style={{ marginBottom:'1.2rem' }}>
                    <InputField label={ui.form_name}    value={form.name}    onChange={set('name')}    error={errors.name} />
                    <InputField label={ui.form_company} value={form.company} onChange={set('company')} />
                    <InputField label={ui.form_phone}   value={form.phone}   onChange={set('phone')}   type="tel" error={errors.phone} />
                    <InputField label={ui.form_email}   value={form.email}   onChange={set('email')}   type="email" error={errors.email} />
                  </div>
                  {/* Service select */}
                  <div style={{ marginBottom:'1.2rem' }}>
                    <label style={{ display:'block', fontSize:'0.8rem', fontWeight:700, letterSpacing:'0.05em', textTransform:'uppercase', color:'var(--navy)', marginBottom:'0.45rem' }}>
                      {ui.form_service}
                    </label>
                    <select value={form.service} onChange={set('service')} style={{ width:'100%', padding:'0.75rem 1rem', border:'1.5px solid rgba(10,25,60,0.15)', borderRadius:10, fontSize:'0.92rem', fontFamily:"'Outfit',sans-serif", background:'white', color:'var(--navy)', outline:'none', cursor:'pointer' }}>
                      <option value="">{ui.form_select}</option>
                      {(ui.service_options||[]).map(s => <option key={s.value} value={s.value}>{s.label}</option>)}
                    </select>
                  </div>
                  <div style={{ marginBottom:'1.8rem' }}>
                    <InputField label={ui.form_message} value={form.message} onChange={set('message')} error={errors.message} textarea />
                  </div>
                  {status === 'error' && (
                    <p style={{ color:'#EF4444', fontSize:'0.88rem', marginBottom:'1rem', padding:'0.75rem 1rem', background:'rgba(239,68,68,0.08)', borderRadius:8 }}>
                      {lang==='fr'?'Une erreur est survenue. Veuillez réessayer.':lang==='en'?'An error occurred. Please try again.':'حدث خطأ. يرجى المحاولة مرة أخرى.'}
                    </p>
                  )}
                  <button type="submit" disabled={status==='loading'} className="btn-solid" style={{ width:'100%', justifyContent:'center', opacity:status==='loading'?0.7:1, cursor:status==='loading'?'not-allowed':'pointer' }}>
                    {status==='loading' ? ui.sending : ui.send}
                  </button>
                </form>
              )}
            </div>
          </Fade>
        </div>
      </section>
    </>
  )
}

function SocBtn({ href, icon }) {
  const [hov, setHov] = useState(false)
  return (
    <a href={href} target="_blank" rel="noreferrer"
      onMouseEnter={() => setHov(true)} onMouseLeave={() => setHov(false)}
      style={{ width:42, height:42, borderRadius:10, border:`1.5px solid ${hov?'var(--green)':'rgba(10,25,60,0.15)'}`, display:'flex', alignItems:'center', justifyContent:'center', color:hov?'var(--green)':'var(--gray)', fontSize:'0.95rem', transition:'all 0.25s' }}>
      <i className={icon} />
    </a>
  )
}
