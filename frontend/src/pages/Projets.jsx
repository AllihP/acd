import { useState } from 'react'
import { Link } from 'react-router-dom'
import { useLang, t } from '../context/LangContext'
import { useInView } from 'react-intersection-observer'

function Fade({ children, delay=0, style={} }) {
  const { ref, inView } = useInView({ threshold:0.1, triggerOnce:true })
  return (
    <div ref={ref} style={{ opacity:inView?1:0, transform:inView?'translateY(0)':'translateY(28px)', transition:`opacity 0.65s ease ${delay}s, transform 0.65s ease ${delay}s`, ...style }}>
      {children}
    </div>
  )
}

function ServiceDetail({ svc, lang, index, expanded, onToggle }) {
  const [hov, setHov] = useState(false)
  return (
    <div
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      style={{ border:`1.5px solid ${expanded?'var(--green)':hov?'rgba(10,25,60,0.25)':'rgba(10,25,60,0.1)'}`, borderRadius:20, overflow:'hidden', transition:'all 0.35s', cursor:'pointer', background: expanded ? 'var(--navy)' : hov ? 'rgba(10,25,60,0.02)' : 'white' }}
      onClick={onToggle}>
      {/* Header */}
      <div style={{ display:'flex', alignItems:'center', gap:'1.5rem', padding:'2rem 2.5rem' }}>
        <div style={{ width:52, height:52, flexShrink:0, borderRadius:14, display:'flex', alignItems:'center', justifyContent:'center', fontSize:'1.3rem', background: expanded ? 'rgba(106,171,46,0.2)' : 'linear-gradient(135deg,var(--navy),var(--blue))', color: expanded ? 'var(--green)' : 'white', transition:'all 0.35s' }}>
          <i className={svc.icon||'fas fa-star'} />
        </div>
        <div style={{ flex:1 }}>
          <div style={{ fontSize:'0.75rem', fontWeight:700, letterSpacing:'0.12em', textTransform:'uppercase', color: expanded ? 'var(--green)' : 'var(--gray)', marginBottom:'0.3rem' }}>
            {String(index+1).padStart(2,'0')}
          </div>
          <h3 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'1.5rem', fontWeight:700, color: expanded ? 'white' : 'var(--navy)', lineHeight:1.2 }}>
            {t(svc,lang,'title')}
          </h3>
        </div>
        <div style={{ width:36, height:36, borderRadius:'50%', border:`1.5px solid ${expanded?'var(--green)':'rgba(10,25,60,0.15)'}`, display:'flex', alignItems:'center', justifyContent:'center', transition:'all 0.35s', transform: expanded ? 'rotate(45deg)' : 'none', color: expanded ? 'var(--green)' : 'var(--navy)', flexShrink:0 }}>
          <i className="fas fa-plus" style={{ fontSize:'0.85rem' }} />
        </div>
      </div>
      {/* Body */}
      {expanded && (
        <div style={{ padding:'0 2.5rem 2.5rem', borderTop:'1px solid rgba(106,171,46,0.2)' }}>
          <p style={{ fontSize:'1rem', color:'rgba(255,255,255,0.7)', lineHeight:1.8, marginTop:'1.5rem' }}>
            {t(svc,lang,'text')}
          </p>
          <Link to="/contact" style={{ display:'inline-flex', alignItems:'center', gap:'0.6rem', marginTop:'1.5rem', color:'var(--green)', fontWeight:600, fontSize:'0.9rem' }}
            onClick={e => e.stopPropagation()}>
            {lang==='fr'?'Demander un devis':lang==='en'?'Request a quote':'طلب عرض سعر'}
            <i className="fas fa-arrow-right" style={{ fontSize:'0.75rem' }} />
          </Link>
        </div>
      )}
    </div>
  )
}

export default function Projets({ data }) {
  const { lang, ui } = useLang()
  const svcs = data?.services || []
  const [expanded, setExpanded] = useState(0)

  const toggle = (i) => setExpanded(expanded === i ? null : i)

  return (
    <>
      {/* Header */}
      <section style={{ background:'var(--navy)', padding:'5rem 3rem 4rem', position:'relative', overflow:'hidden' }}>
        <div style={{ position:'absolute', top:0, right:0, width:'40%', height:'100%', background:'var(--navy2)', clipPath:'polygon(15% 0,100% 0,100% 100%,0 100%)', opacity:0.5 }} />
        <div style={{ position:'relative', zIndex:2, maxWidth:1440, margin:'0 auto' }}>
          <p style={{ fontSize:'0.78rem', fontWeight:700, letterSpacing:'0.18em', textTransform:'uppercase', color:'var(--green)', marginBottom:'1rem' }}>
            {ui.svc_eyebrow}
          </p>
          <h1 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'clamp(2.8rem,4vw,5.5rem)', fontWeight:700, lineHeight:1.05, color:'white', maxWidth:700 }}>
            {lang==='fr'?'Nos services & expertises':lang==='en'?'Our Services & Expertise':'خدماتنا وخبراتنا'}
          </h1>
          <p style={{ fontSize:'1rem', color:'rgba(255,255,255,0.55)', marginTop:'1rem', maxWidth:520 }}>
            {lang==='fr'?'Des solutions complètes adaptées à chaque besoin.':lang==='en'?'Complete solutions tailored to every need.':'حلول متكاملة مصممة لكل احتياج.'}
          </p>
        </div>
      </section>

      {/* Services accordion */}
      <section className="section" style={{ background:'var(--cream)' }}>
        <div style={{ maxWidth:1440, margin:'0 auto' }}>
          <div className="responsive-grid-contact" style={{ gap:'3rem' }}>
            {/* Left: intro */}
            <Fade>
              <div style={{ position:'sticky', top:100 }}>
                <p className="sec-eyebrow">{ui.svc_eyebrow}</p>
                <h2 className="sec-title">
                  {lang==='fr'?'Ce que nous faisons':lang==='en'?'What We Do':'ما نقدمه'}
                </h2>
                <p className="sec-subtitle" style={{ marginBottom:'2.5rem' }}>
                  {lang==='fr'?"Chaque service est pensé pour apporter une valeur mesurable à votre organisation."
                  :lang==='en'?"Every service is designed to bring measurable value to your organization."
                  :"كل خدمة مصممة لتقديم قيمة قابلة للقياس لمؤسستك."}
                </p>
                {/* Stats */}
                <div className="responsive-grid-2" style={{ gap:'1rem' }}>
                  {[
                    { n: svcs.length, label: lang==='fr'?'Services':lang==='en'?'Services':'خدمة' },
                    { n: data?.portfolio?.length||0, label: lang==='fr'?'Réalisations':lang==='en'?'Projects':'إنجاز' },
                  ].map((s,i) => (
                    <div key={i} style={{ background:'var(--navy)', borderRadius:16, padding:'1.5rem 2rem', textAlign:'center' }}>
                      <div style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'2.8rem', fontWeight:700, color:'var(--gold)', lineHeight:1 }}>{s.n}+</div>
                      <div style={{ fontSize:'0.8rem', color:'rgba(255,255,255,0.55)', letterSpacing:'0.08em', textTransform:'uppercase', marginTop:'0.3rem' }}>{s.label}</div>
                    </div>
                  ))}
                </div>
                <div style={{ marginTop:'2rem' }}>
                  <Link to="/contact" className="btn-solid">
                    {lang==='fr'?'Discuter de votre projet':lang==='en'?'Discuss your project':'ناقش مشروعك'}
                    <i className="fas fa-arrow-right" />
                  </Link>
                </div>
              </div>
            </Fade>

            {/* Right: accordion */}
            <div style={{ display:'flex', flexDirection:'column', gap:'1rem' }}>
              {svcs.length === 0 ? (
                <div style={{ textAlign:'center', padding:'4rem', color:'var(--gray)' }}>
                  <i className="fas fa-cogs" style={{ fontSize:'3rem', opacity:0.3, display:'block', marginBottom:'1rem' }} />
                  <p>{lang==='fr'?'Aucun service configuré.':lang==='en'?'No services configured.':'لا توجد خدمات.'}</p>
                </div>
              ) : (
                svcs.map((svc,i) => (
                  <Fade key={svc.id} delay={i*0.07}>
                    <ServiceDetail svc={svc} lang={lang} index={i} expanded={expanded===i} onToggle={() => toggle(i)} />
                  </Fade>
                ))
              )}
            </div>
          </div>
        </div>
      </section>

      {/* CTA Banner */}
      <section className="section" style={{ background:'var(--navy)', textAlign:'center' }}>
        <div style={{ maxWidth:700, margin:'0 auto' }}>
          <Fade>
            <h2 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'clamp(2rem,3.5vw,3.5rem)', fontWeight:700, color:'white', marginBottom:'1.2rem', lineHeight:1.1 }}>
              {lang==='fr'?'Prêt à transformer votre communication ?':lang==='en'?'Ready to transform your communication?':'هل أنت مستعد لتحويل تواصلك؟'}
            </h2>
            <p style={{ color:'rgba(255,255,255,0.6)', fontSize:'1.05rem', lineHeight:1.7, marginBottom:'2.5rem' }}>
              {lang==='fr'?'Consultation gratuite. Réponse en 48h.':lang==='en'?'Free consultation. Reply within 48h.':'استشارة مجانية. رد خلال 48 ساعة.'}
            </p>
            <Link to="/contact" className="btn-solid" style={{ justifyContent:'center' }}>
              {lang==='fr'?'Démarrer maintenant':lang==='en'?'Start Now':'ابدأ الآن'}
              <i className="fas fa-arrow-right" />
            </Link>
          </Fade>
        </div>
      </section>
    </>
  )
}
