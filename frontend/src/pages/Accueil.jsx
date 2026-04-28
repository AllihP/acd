import { useEffect, useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import { useLang, t } from '../context/LangContext'
import { useInView } from 'react-intersection-observer'

function StatItem({ value, label, active }) {
  const ref = useRef(null)
  useEffect(() => {
    if (!active || !ref.current) return
    let cur = 0; const step = value / 70
    const timer = setInterval(() => {
      cur = Math.min(cur + step, value)
      if (ref.current) ref.current.textContent = Math.floor(cur) + (value >= 100 ? '+' : '')
      if (cur >= value) clearInterval(timer)
    }, 18)
    return () => clearInterval(timer)
  }, [active, value])
  return (
    <div>
      <div style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'3.2rem', fontWeight:700, color:'var(--gold)', lineHeight:1 }}>
        <span ref={ref}>0</span>
      </div>
      <div style={{ fontSize:'0.82rem', color:'rgba(255,255,255,0.5)', letterSpacing:'0.05em', textTransform:'uppercase', marginTop:'0.3rem' }}>
        {label}
      </div>
    </div>
  )
}

function Fade({ children, delay=0, style={} }) {
  const { ref, inView } = useInView({ threshold:0.12, triggerOnce:true })
  return (
    <div ref={ref} style={{ opacity:inView?1:0, transform:inView?'translateY(0)':'translateY(32px)', transition:`opacity 0.7s ease ${delay}s, transform 0.7s ease ${delay}s`, ...style }}>
      {children}
    </div>
  )
}

function ServiceCard({ svc, lang, index }) {
  const [hov, setHov] = useState(false)
  const { ref, inView } = useInView({ threshold:0.1, triggerOnce:true })
  return (
    <div ref={ref} onMouseEnter={() => setHov(true)} onMouseLeave={() => setHov(false)}
      style={{ background:hov?'var(--navy)':'white', padding:'2.8rem 2.4rem', position:'relative',
        transition:'background 0.4s', opacity:inView?1:0, transform:inView?'translateY(0)':'translateY(20px)',
        transitionDelay:`${index*0.07}s` }}>
      <div style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'4.5rem', fontWeight:700, color:hov?'rgba(106,171,46,0.2)':'rgba(10,25,60,0.07)', lineHeight:1, marginBottom:'1rem', userSelect:'none', transition:'color 0.4s' }}>
        {String(index+1).padStart(2,'0')}
      </div>
      <div style={{ width:52, height:52, background:hov?'linear-gradient(135deg,var(--green),var(--green2))':'linear-gradient(135deg,var(--navy),var(--blue))', borderRadius:14, display:'flex', alignItems:'center', justifyContent:'center', color:'white', fontSize:'1.3rem', marginBottom:'1.5rem', transform:hov?'rotate(6deg) scale(1.08)':'none', transition:'all 0.4s' }}>
        <i className={svc.icon||'fas fa-star'} />
      </div>
      <h3 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'1.55rem', fontWeight:700, color:hov?'white':'var(--navy)', marginBottom:'0.8rem', transition:'color 0.4s' }}>
        {t(svc,lang,'title')}
      </h3>
      <p style={{ fontSize:'0.9rem', color:hov?'rgba(255,255,255,0.65)':'var(--gray)', lineHeight:1.7, transition:'color 0.4s' }}>
        {t(svc,lang,'text')}
      </p>
    </div>
  )
}

function WhyCard({ item, lang, index }) {
  const [hov, setHov] = useState(false)
  return (
    <div onMouseEnter={() => setHov(true)} onMouseLeave={() => setHov(false)}
      style={{ border:`1px solid ${hov?'var(--green)':'rgba(255,255,255,0.1)'}`, background:hov?'rgba(106,171,46,0.06)':'transparent', borderRadius:20, padding:'3rem 2.5rem', position:'relative', overflow:'hidden', transition:'all 0.4s', cursor:'default' }}>
      <div style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'5rem', fontWeight:700, color:'rgba(255,255,255,0.05)', position:'absolute', top:'1.5rem', right:'2rem', lineHeight:1, userSelect:'none' }}>
        {String(index+1).padStart(2,'0')}
      </div>
      <div style={{ width:48, height:48, background:'rgba(106,171,46,0.15)', borderRadius:12, display:'flex', alignItems:'center', justifyContent:'center', color:'var(--green)', fontSize:'1.3rem', marginBottom:'1.5rem' }}>
        <i className={item.icon||'fas fa-check'} />
      </div>
      <h3 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'1.6rem', fontWeight:700, color:'white', marginBottom:'0.8rem', lineHeight:1.2 }}>
        {t(item,lang,'title')}
      </h3>
      <p style={{ fontSize:'0.9rem', color:'rgba(255,255,255,0.55)', lineHeight:1.7 }}>{t(item,lang,'text')}</p>
    </div>
  )
}

function TestiCard({ testi, lang }) {
  const [hov, setHov] = useState(false)
  return (
    <div onMouseEnter={() => setHov(true)} onMouseLeave={() => setHov(false)}
      style={{ background:'white', borderRadius:20, padding:'2.5rem 2rem', boxShadow:hov?'0 16px 40px rgba(12,25,49,0.12)':'0 4px 24px rgba(12,25,49,0.06)', transform:hov?'translateY(-6px)':'none', transition:'all 0.3s' }}>
      <div style={{ color:'var(--gold)', fontSize:'1.1rem', marginBottom:'1rem' }}>{'★'.repeat(testi.rating||5)}</div>
      <p style={{ fontSize:'0.95rem', color:'var(--gray)', lineHeight:1.7, marginBottom:'1.5rem', fontStyle:'italic' }}>
        « {t(testi,lang,'text')} »
      </p>
      <div style={{ display:'flex', alignItems:'center', gap:'1rem' }}>
        {testi.avatar_url
          ? <img src={testi.avatar_url} alt={testi.author} style={{ width:48, height:48, borderRadius:'50%', objectFit:'cover' }} />
          : <div style={{ width:48, height:48, borderRadius:'50%', background:'linear-gradient(135deg,var(--navy),var(--blue))', display:'flex', alignItems:'center', justifyContent:'center', color:'white', fontWeight:700 }}>{testi.author?.[0]}</div>
        }
        <div>
          <div style={{ fontWeight:700, color:'var(--navy)', fontSize:'0.95rem' }}>{testi.author}</div>
          <div style={{ fontSize:'0.82rem', color:'var(--green)', fontWeight:600 }}>{t(testi,lang,'role')}{testi.company?` — ${testi.company}`:''}</div>
        </div>
      </div>
    </div>
  )
}

const RIBBON = ['Branding','Marketing Digital','Événementiel','Social Media','Audiovisuel','Print','Stratégie','Conseil']

const AGENCY_NAME = {
  fr: "AGENCE DE COMMUNICATION POUR LE DÉVELOPPEMENT",
  en: "COMMUNICATION AGENCY FOR DEVELOPMENT",
  ar: "وكالة الاتصال من أجل التنمية"
};

const HERO_WORDS = {
  fr: ["Communication", "Marketing", "Événementiel"],
  en: ["Communication", "Marketing", "Events"],
  ar: ["الاتصال", "التسويق", "الفعاليات"]
};

export default function Accueil({ data }) {
  const { lang, ui } = useLang()
  const hero   = data?.hero         || {}
  const svcs   = data?.services     || []
  const whys   = data?.why_items    || []
  const testis = data?.testimonials || []
  const { ref: heroRef, inView: heroInView } = useInView({ threshold:0.3, triggerOnce:true })

  const agencyName = AGENCY_NAME[lang] || AGENCY_NAME.fr;
  const [w1, w2, w3] = HERO_WORDS[lang] || HERO_WORDS.fr;

  return (
    <>
      {/* HERO */}
      <section id="accueil" ref={heroRef} style={{ position:'relative', minHeight:'92vh', background:'var(--navy)', overflow:'hidden', display:'flex', alignItems:'center' }}>
        <div style={{ position:'absolute', top:0, right:0, width:'55%', height:'100%', background:'var(--navy2)', clipPath:'polygon(12% 0, 100% 0, 100% 100%, 0% 100%)' }} />
        {hero.bg_image_url && <img src={hero.bg_image_url} alt="" style={{ position:'absolute', top:0, right:0, width:'55%', height:'100%', objectFit:'cover', opacity:0.45, clipPath:'polygon(12% 0, 100% 0, 100% 100%, 0% 100%)' }} />}
        <div style={{ position:'relative', zIndex:2, maxWidth:1440, margin:'0 auto', padding:'0 3rem', width:'100%' }}>
          <div style={{ display:'inline-flex', alignItems:'center', gap:'0.6rem', background:'linear-gradient(90deg, rgba(106,171,46,0.2) 0%, rgba(106,171,46,0.05) 100%)', borderLeft:'3px solid var(--green)', color:'var(--green)', padding:'0.5rem 1.2rem', borderRadius:'0 8px 8px 0', fontSize:'0.85rem', fontWeight:800, letterSpacing:'0.15em', textTransform:'uppercase', marginBottom:'2.5rem', opacity:heroInView?1:0, transition:'opacity 0.8s ease 0.2s', boxShadow:'0 4px 15px rgba(0,0,0,0.1)' }}>
            <span style={{ width:8, height:8, background:'var(--green)', borderRadius:'50%', animation:'blink 2s ease-in-out infinite', flexShrink:0, boxShadow:'0 0 10px var(--green)' }} />
            {agencyName}
          </div>
          <h1 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'clamp(3rem,5.5vw,6.5rem)', fontWeight:700, lineHeight:1.1, letterSpacing:'-0.01em', color:'white', maxWidth:800, marginBottom:'2.2rem', opacity:heroInView?1:0, transform:heroInView?'translateY(0)':'translateY(30px)', transition:'opacity 0.8s ease 0.35s, transform 0.8s ease 0.35s' }}>
            <span style={{ color: 'transparent', WebkitTextStroke: '1px rgba(255,255,255,0.8)', backgroundImage: 'linear-gradient(45deg, #fff, #f0f0f0)', WebkitBackgroundClip: 'text', backgroundClip: 'text' }}>{w1}</span>
            <span style={{ color:'var(--gold)', margin:'0 0.4rem' }}>—</span>
            <span style={{ background:'linear-gradient(120deg, var(--green), #a2e061)', WebkitBackgroundClip:'text', WebkitTextFillColor:'transparent' }}>{w2}</span>
            <span style={{ color:'var(--gold)', margin:'0 0.4rem' }}>—</span>
            <span>{w3}</span>
          </h1>
          <p style={{ fontSize:'1.15rem', color:'rgba(255,255,255,0.75)', maxWidth:600, lineHeight:1.8, marginBottom:'3rem', opacity:heroInView?1:0, transition:'opacity 0.8s ease 0.5s', fontWeight:300 }}>
            {t(hero,lang,'subtitle') || 'Nous donnons vie à vos idées et propulsons votre marque vers l\'excellence avec des stratégies innovantes et percutantes.'}
          </p>
          <div style={{ display:'flex', gap:'1.2rem', flexWrap:'wrap', alignItems:'center', marginBottom:'5rem', opacity:heroInView?1:0, transition:'opacity 0.8s ease 0.65s' }}>
            <Link to="/contact" className="btn-solid">{t(hero,lang,'cta1')||'Contact'} <i className="fas fa-arrow-right" /></Link>
            <Link to="/realisations" className="btn-outline">{t(hero,lang,'cta2')||'Réalisations'} <i className="fas fa-play" style={{ fontSize:'0.75rem' }} /></Link>
          </div>
          <div style={{ display:'flex', gap:'3rem', paddingTop:'3rem', borderTop:'1px solid rgba(255,255,255,0.1)', opacity:heroInView?1:0, transition:'opacity 0.8s ease 0.8s' }}>
            <StatItem value={hero.stat1_value||120} label={t(hero,lang,'stat1_label')} active={heroInView} />
            <StatItem value={hero.stat2_value||8}   label={t(hero,lang,'stat2_label')} active={heroInView} />
            <StatItem value={hero.stat3_value||98}  label={t(hero,lang,'stat3_label')} active={heroInView} />
          </div>
        </div>
        <style>{`@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}`}</style>
      </section>

      {/* RIBBON */}
      <div className="ribbon"><div className="ribbon-track">
        {[...RIBBON,...RIBBON].map((item,i) => <span className="ribbon-item" key={i}>{item} <span className="ribbon-dot">◆</span></span>)}
      </div></div>

      {/* SERVICES */}
      {svcs.length > 0 && (
        <section id="services" style={{ background:'white', padding:'6rem 3rem' }}>
          <div style={{ maxWidth:1440, margin:'0 auto' }}>
            <Fade style={{ marginBottom:'4rem' }}>
              <p className="sec-eyebrow">{ui.svc_eyebrow}</p>
              <h2 className="sec-title">{lang==='fr'?'Des solutions sur-mesure pour un impact réel':lang==='en'?'Tailored solutions for real impact':'حلول مخصصة لتأثير حقيقي'}</h2>
              <p className="sec-subtitle">{lang==='fr'?'Du digital au terrain, nous maîtrisons tous les leviers pour propulser votre marque.':lang==='en'?'From digital to on-ground, we master every lever to elevate your brand.':'من الرقمي إلى الميداني، نتحكم في كل الروافع لرفع علامتك التجارية.'}</p>
            </Fade>
            <div style={{ display:'grid', gridTemplateColumns:'repeat(auto-fit,minmax(280px,1fr))', gap:'1.5px', background:'rgba(10,25,60,0.08)', borderRadius:20, overflow:'hidden' }}>
              {svcs.map((svc,i) => <ServiceCard key={svc.id} svc={svc} lang={lang} index={i} />)}
            </div>
          </div>
        </section>
      )}

      {/* WHY ACD */}
      {whys.length > 0 && (
        <section style={{ background:'var(--navy)', padding:'6rem 3rem' }}>
          <div style={{ maxWidth:1440, margin:'0 auto' }}>
            <Fade>
              <p className="sec-eyebrow">{ui.why_eyebrow}</p>
              <h2 className="sec-title" style={{ color:'white' }}>{lang==='fr'?'Les raisons pour lesquelles les leaders choisissent ACD':lang==='en'?'Why industry leaders choose ACD':'لماذا يختار القادة وكالة ACD'}</h2>
            </Fade>
            <div style={{ display:'grid', gridTemplateColumns:'repeat(auto-fit,minmax(280px,1fr))', gap:'2.5rem', marginTop:'4rem' }}>
              {whys.map((item,i) => <Fade key={item.id} delay={i*0.1}><WhyCard item={item} lang={lang} index={i} /></Fade>)}
            </div>
          </div>
        </section>
      )}

      {/* TESTIMONIALS */}
      {testis.length > 0 && (
        <section style={{ background:'var(--cream)', padding:'6rem 3rem' }}>
          <div style={{ maxWidth:1440, margin:'0 auto' }}>
            <Fade style={{ textAlign:'center', marginBottom:'4rem' }}>
              <p className="sec-eyebrow">{ui.testi_eyebrow}</p>
              <h2 className="sec-title">{ui.testi_title}</h2>
            </Fade>
            <div style={{ display:'grid', gridTemplateColumns:'repeat(auto-fit,minmax(300px,1fr))', gap:'2rem' }}>
              {testis.map((testi,i) => <Fade key={testi.id} delay={i*0.1}><TestiCard testi={testi} lang={lang} /></Fade>)}
            </div>
          </div>
        </section>
      )}
    </>
  )
}
