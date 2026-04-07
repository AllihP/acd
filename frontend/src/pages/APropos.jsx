import { useLang, t } from '../context/LangContext'
import { useInView } from 'react-intersection-observer'
import { Link } from 'react-router-dom'

function Fade({ children, delay=0, style={} }) {
  const { ref, inView } = useInView({ threshold:0.12, triggerOnce:true })
  return (
    <div ref={ref} style={{ opacity:inView?1:0, transform:inView?'translateY(0)':'translateY(28px)', transition:`opacity 0.7s ease ${delay}s, transform 0.7s ease ${delay}s`, ...style }}>
      {children}
    </div>
  )
}

function FactCard({ label, value }) {
  return (
    <div style={{ padding:'1.5rem 2rem', border:'1px solid rgba(10,25,60,0.08)', borderRadius:16, transition:'all 0.3s', cursor:'default' }}
      onMouseEnter={e => { e.currentTarget.style.borderColor='var(--green)'; e.currentTarget.style.background='rgba(106,171,46,0.04)' }}
      onMouseLeave={e => { e.currentTarget.style.borderColor='rgba(10,25,60,0.08)'; e.currentTarget.style.background='transparent' }}>
      <div style={{ fontSize:'0.75rem', fontWeight:700, letterSpacing:'0.12em', textTransform:'uppercase', color:'var(--green)', marginBottom:'0.5rem' }}>{label}</div>
      <div style={{ fontSize:'1.05rem', fontWeight:600, color:'var(--navy)' }}>{value}</div>
    </div>
  )
}

export default function APropos({ data }) {
  const { lang, ui } = useLang()
  const about = data?.about || {}

  return (
    <>
      {/* Page Header */}
      <section style={{ background:'var(--navy)', padding:'5rem 3rem 4rem', position:'relative', overflow:'hidden' }}>
        <div style={{ position:'absolute', top:0, right:0, width:'40%', height:'100%', background:'var(--navy2)', clipPath:'polygon(15% 0,100% 0,100% 100%,0 100%)', opacity:0.5 }} />
        <div style={{ position:'relative', zIndex:2, maxWidth:1440, margin:'0 auto' }}>
          <p style={{ fontSize:'0.78rem', fontWeight:700, letterSpacing:'0.18em', textTransform:'uppercase', color:'var(--green)', marginBottom:'1rem' }}>
            {t(about,lang,'eyebrow')||ui.nav_about}
          </p>
          <h1 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'clamp(2.8rem,4vw,5.5rem)', fontWeight:700, lineHeight:1.05, color:'white', maxWidth:700 }}>
            {t(about,lang,'title')||"Nés à N'Djamena. Rayonnons en Afrique."}
          </h1>
        </div>
      </section>

      {/* Main content */}
      <section style={{ background:'white', padding:'6rem 3rem' }}>
        <div style={{ maxWidth:1440, margin:'0 auto' }}>
          <div style={{ display:'grid', gridTemplateColumns:'1fr 1.1fr', gap:'6rem', alignItems:'center' }}>
            {/* Image */}
            <Fade>
              <div style={{ position:'relative', aspectRatio:'4/5' }}>
                <div style={{ borderRadius:24, overflow:'hidden', width:'100%', height:'100%', background:'linear-gradient(135deg,var(--navy),var(--blue))', display:'flex', alignItems:'center', justifyContent:'center' }}>
                  {about.image_url
                    ? <img src={about.image_url} alt="À propos ACD" style={{ width:'100%', height:'100%', objectFit:'cover' }} />
                    : <div style={{ textAlign:'center', color:'rgba(255,255,255,0.5)' }}>
                        <i className="fas fa-image" style={{ fontSize:'4rem', marginBottom:'1rem', display:'block' }} />
                        <span style={{ fontSize:'0.9rem' }}>Ajoutez votre image<br/>depuis l'admin</span>
                      </div>
                  }
                </div>
                {/* Badge */}
                <div style={{ position:'absolute', bottom:'2rem', right:'-2rem', background:'var(--green)', color:'white', borderRadius:16, padding:'1.5rem 2rem', textAlign:'center', boxShadow:'0 20px 50px rgba(106,171,46,0.4)' }}>
                  <div style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'3rem', fontWeight:700, lineHeight:1 }}>
                    {about.years_exp || 8}
                  </div>
                  <div style={{ fontSize:'0.75rem', fontWeight:700, letterSpacing:'0.08em', textTransform:'uppercase', marginTop:'0.3rem', opacity:0.9 }}>
                    {ui.years_exp}
                  </div>
                </div>
              </div>
            </Fade>

            {/* Text */}
            <div>
              <Fade delay={0.1}>
                <p className="sec-eyebrow">{t(about,lang,'eyebrow')||'— Notre histoire'}</p>
                <h2 className="sec-title" style={{ marginBottom:'1.5rem' }}>
                  {t(about,lang,'title')||"Nés à N'Djamena. Rayonnons en Afrique."}
                </h2>
                <p style={{ fontSize:'1.05rem', color:'var(--gray)', lineHeight:1.8, marginBottom:'2.5rem' }}>
                  {t(about,lang,'text')||"L'ACD n'est pas une agence ordinaire. Nous sommes un moteur de développement."}
                </p>
              </Fade>

              {/* Facts grid */}
              <div style={{ display:'grid', gridTemplateColumns:'1fr 1fr', gap:'1rem', marginBottom:'2.5rem' }}>
                {[
                  { lk:'fact1_label', vk:'fact1_value' },
                  { lk:'fact2_label', vk:'fact2_value' },
                  { lk:'fact3_label', vk:'fact3_value' },
                  { lk:'fact4_label', vk:'fact4_value' },
                ].map((f,i) => (
                  <Fade key={i} delay={0.2 + i*0.1}>
                    <FactCard label={t(about,lang,f.lk)} value={t(about,lang,f.vk)} />
                  </Fade>
                ))}
              </div>

              <Fade delay={0.5}>
                <Link to="/contact" className="btn-solid">
                  {t(about,lang,'cta')||ui.nav_contact}
                  <i className="fas fa-arrow-right" />
                </Link>
              </Fade>
            </div>
          </div>
        </div>
      </section>

      {/* Values strip */}
      <section style={{ background:'var(--cream)', padding:'5rem 3rem' }}>
        <div style={{ maxWidth:1440, margin:'0 auto' }}>
          <Fade style={{ textAlign:'center', marginBottom:'3rem' }}>
            <h2 className="sec-title">
              {lang==='fr'?'Nos valeurs fondamentales':lang==='en'?'Our Core Values':'قيمنا الأساسية'}
            </h2>
          </Fade>
          <div style={{ display:'grid', gridTemplateColumns:'repeat(auto-fit,minmax(200px,1fr))', gap:'2rem' }}>
            {[
              { icon:'fas fa-lightbulb', label:lang==='fr'?'Innovation':lang==='en'?'Innovation':'الابتكار' },
              { icon:'fas fa-handshake', label:lang==='fr'?'Confiance':lang==='en'?'Trust':'الثقة' },
              { icon:'fas fa-globe-africa', label:lang==='fr'?'Ancrage local':lang==='en'?'Local roots':'الجذور المحلية' },
              { icon:'fas fa-chart-line', label:lang==='fr'?'Excellence':lang==='en'?'Excellence':'التميز' },
              { icon:'fas fa-users', label:lang==='fr'?'Collaboration':lang==='en'?'Collaboration':'التعاون' },
            ].map((v,i) => (
              <Fade key={i} delay={i*0.08} style={{ textAlign:'center' }}>
                <div style={{ width:64, height:64, background:'var(--navy)', borderRadius:18, display:'flex', alignItems:'center', justifyContent:'center', margin:'0 auto 1rem', transition:'all 0.3s' }}
                  onMouseEnter={e => { e.currentTarget.style.background='var(--green)'; e.currentTarget.style.transform='translateY(-4px) rotate(6deg)' }}
                  onMouseLeave={e => { e.currentTarget.style.background='var(--navy)'; e.currentTarget.style.transform='none' }}>
                  <i className={v.icon} style={{ color:'var(--gold)', fontSize:'1.4rem' }} />
                </div>
                <p style={{ fontWeight:700, color:'var(--navy)', fontSize:'0.95rem' }}>{v.label}</p>
              </Fade>
            ))}
          </div>
        </div>
      </section>
    </>
  )
}
