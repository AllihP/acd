import { useState } from 'react'
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

function PfCard({ item, lang }) {
  const [hov, setHov] = useState(false)
  return (
    <div onMouseEnter={() => setHov(true)} onMouseLeave={() => setHov(false)}
      style={{ borderRadius:16, overflow:'hidden', position:'relative', height:300, cursor:'pointer',
        boxShadow: hov ? '0 20px 50px rgba(12,25,49,0.2)' : '0 4px 16px rgba(12,25,49,0.08)',
        transform: hov ? 'translateY(-6px)' : 'none', transition:'all 0.4s' }}>
      {item.image_url
        ? <img src={item.image_url} alt={t(item,lang,'title')} style={{ width:'100%', height:'100%', objectFit:'cover', transform:hov?'scale(1.08)':'scale(1)', transition:'transform 0.7s ease' }} />
        : <div style={{ width:'100%', height:'100%', background:'linear-gradient(135deg,var(--navy),var(--blue))', display:'flex', alignItems:'center', justifyContent:'center' }}>
            <i className="fas fa-image" style={{ fontSize:'3rem', color:'rgba(255,255,255,0.2)' }} />
          </div>
      }
      <div style={{ position:'absolute', inset:0, background:'linear-gradient(180deg,transparent 40%,rgba(12,25,49,0.92) 100%)', display:'flex', flexDirection:'column', justifyContent:'flex-end', padding:'1.8rem', color:'white', opacity:hov?1:0.7, transition:'opacity 0.4s' }}>
        <span style={{ fontSize:'0.78rem', color:'var(--green)', fontWeight:700, letterSpacing:'0.1em', textTransform:'uppercase', marginBottom:'0.4rem' }}>
          {item.category_display || item.category}
          {item.year ? ` · ${item.year}` : ''}
          {item.client ? ` · ${item.client}` : ''}
        </span>
        <h3 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'1.35rem', fontWeight:700 }}>
          {t(item,lang,'title')}
        </h3>
        {t(item,lang,'description') && (
          <p style={{ fontSize:'0.82rem', color:'rgba(255,255,255,0.7)', marginTop:'0.4rem', lineHeight:1.5,
            maxHeight: hov ? '60px' : 0, overflow:'hidden', transition:'max-height 0.4s' }}>
            {t(item,lang,'description')}
          </p>
        )}
        {item.is_featured && (
          <span style={{ position:'absolute', top:'1rem', right:'1rem', background:'var(--gold)', color:'var(--navy)', fontSize:'0.72rem', fontWeight:700, padding:'0.25rem 0.7rem', borderRadius:9999, letterSpacing:'0.05em' }}>
            ★ Featured
          </span>
        )}
      </div>
    </div>
  )
}

export default function Realisations({ data }) {
  const { lang, ui } = useLang()
  const portfolio = data?.portfolio || []
  const [activeFilter, setActiveFilter] = useState('all')

  const cats = [
    { key:'all',          label: ui.cat_all },
    { key:'branding',     label: ui.cat_branding },
    { key:'digital',      label: ui.cat_digital },
    { key:'evenement',    label: ui.cat_evenement },
    { key:'print',        label: ui.cat_print },
    { key:'social',       label: ui.cat_social },
    { key:'audiovisuel',  label: ui.cat_audiovisuel },
  ]

  const usedCats = new Set(portfolio.map(p => p.category))
  const visibleCats = cats.filter(c => c.key === 'all' || usedCats.has(c.key))
  const filtered = activeFilter === 'all' ? portfolio : portfolio.filter(p => p.category === activeFilter)

  return (
    <>
      {/* Header */}
      <section style={{ background:'var(--navy)', padding:'5rem 3rem 4rem', position:'relative', overflow:'hidden' }}>
        <div style={{ position:'absolute', top:0, right:0, width:'40%', height:'100%', background:'var(--navy2)', clipPath:'polygon(15% 0,100% 0,100% 100%,0 100%)', opacity:0.5 }} />
        <div style={{ position:'relative', zIndex:2, maxWidth:1440, margin:'0 auto' }}>
          <p style={{ fontSize:'0.78rem', fontWeight:700, letterSpacing:'0.18em', textTransform:'uppercase', color:'var(--green)', marginBottom:'1rem' }}>
            {ui.pf_eyebrow}
          </p>
          <h1 style={{ fontFamily:"'Cormorant Garamond',serif", fontSize:'clamp(2.8rem,4vw,5.5rem)', fontWeight:700, lineHeight:1.05, color:'white', maxWidth:700 }}>
            {lang==='fr'?"Projets qui ont marqué le Tchad":lang==='en'?"Projects that shaped Chad":"مشاريع رسمت معالم تشاد"}
          </h1>
          <p style={{ fontSize:'1rem', color:'rgba(255,255,255,0.55)', marginTop:'1rem', maxWidth:550 }}>
            {lang==='fr'?`${filtered.length} réalisation${filtered.length>1?'s':''} — Découvrez notre savoir-faire`
            :lang==='en'?`${filtered.length} project${filtered.length>1?'s':''} — Discover our expertise`
            :`${filtered.length} مشروع — اكتشف خبراتنا`}
          </p>
        </div>
      </section>

      {/* Portfolio grid */}
      <section style={{ background:'var(--cream)', padding:'5rem 3rem' }}>
        <div style={{ maxWidth:1440, margin:'0 auto' }}>
          {/* Filters */}
          <div style={{ display:'flex', gap:'0.6rem', flexWrap:'wrap', marginBottom:'3rem' }}>
            {visibleCats.map(c => (
              <button key={c.key} onClick={() => setActiveFilter(c.key)} style={{
                padding:'0.5rem 1.4rem', borderRadius:9999,
                border: `1.5px solid ${activeFilter===c.key?'var(--navy)':'rgba(10,25,60,0.15)'}`,
                background: activeFilter===c.key ? 'var(--navy)' : 'transparent',
                color: activeFilter===c.key ? 'white' : 'var(--gray)',
                fontSize:'0.85rem', fontWeight:500, cursor:'pointer',
                transition:'all 0.25s', fontFamily:"'Outfit',sans-serif"
              }}>
                {c.label}
              </button>
            ))}
          </div>

          {/* Grid */}
          {filtered.length === 0 ? (
            <div style={{ textAlign:'center', padding:'5rem', color:'var(--gray)' }}>
              <i className="fas fa-folder-open" style={{ fontSize:'3rem', opacity:0.3, marginBottom:'1rem', display:'block' }} />
              <p>{lang==='fr'?'Aucune réalisation dans cette catégorie.':lang==='en'?'No projects in this category.':'لا توجد مشاريع في هذه الفئة.'}</p>
            </div>
          ) : (
            <div style={{ display:'grid', gridTemplateColumns:'repeat(auto-fill,minmax(320px,1fr))', gap:'1.5rem' }}>
              {filtered.map((item,i) => (
                <Fade key={item.id} delay={i*0.06}>
                  <PfCard item={item} lang={lang} />
                </Fade>
              ))}
            </div>
          )}
        </div>
      </section>
    </>
  )
}
