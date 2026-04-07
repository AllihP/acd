import { useState, useEffect } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import { useLang } from '../context/LangContext'

export default function Navbar({ settings }) {
  const { lang, setLang, ui } = useLang()
  const [scrolled, setScrolled]   = useState(false)
  const [menuOpen, setMenuOpen]   = useState(false)
  const location = useLocation()
  const navigate = useNavigate()

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40)
    window.addEventListener('scroll', onScroll)
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  useEffect(() => { setMenuOpen(false) }, [location])

  const links = [
    { to: '/',             label: ui.nav_home },
    { to: '/a-propos',     label: ui.nav_about },
    { to: '/realisations', label: ui.nav_realisations },
    { to: '/projets',      label: ui.nav_projets },
    { to: '/contact',      label: ui.nav_contact },
  ]

  const isActive = (to) => location.pathname === to

  return (
    <nav id="navbar" style={{
      position: 'sticky', top: 0, width: '100%',
      background: 'rgba(255,255,255,0.97)',
      backdropFilter: 'blur(20px)',
      borderBottom: '1px solid rgba(10,25,60,0.08)',
      zIndex: 999,
      boxShadow: scrolled ? '0 6px 40px rgba(10,25,60,0.12)' : 'none',
      transition: 'box-shadow 0.4s ease'
    }}>
      <div style={{
        maxWidth: 1440, margin: '0 auto', padding: '0 3rem',
        height: 78, display: 'flex', alignItems: 'center',
        justifyContent: 'space-between', gap: '2rem'
      }}>
        {/* Logo */}
        <Link to="/" style={{
          fontFamily: "'Cormorant Garamond', serif",
          fontSize: '1.7rem', fontWeight: 700, color: 'var(--navy)',
          letterSpacing: '0.06em', transition: 'transform 0.3s'
        }}>
          <img src="/logo.png" alt="ACD" style={{ height: 48 }} />
        </Link>

        {/* Desktop Links */}
        <ul style={{ display: 'flex', alignItems: 'center', gap: 0, listStyle: 'none' }}
            className="nav-links-desktop">
          {links.map(l => (
            <li key={l.to}>
              <Link to={l.to} style={{
                position: 'relative', padding: '0.4rem 1.2rem',
                fontSize: '0.92rem', fontWeight: 500,
                color: isActive(l.to) ? 'var(--green2)' : 'var(--navy)',
                letterSpacing: '0.02em', transition: 'color 0.3s',
                display: 'block'
              }}>
                {l.label}
                <span style={{
                  position: 'absolute', bottom: -2, left: '50%',
                  transform: 'translateX(-50%)',
                  width: isActive(l.to) ? '60%' : 0,
                  height: 2, background: 'var(--green)',
                  transition: 'width 0.3s', borderRadius: 2,
                  display: 'block'
                }} />
              </Link>
            </li>
          ))}
        </ul>

        {/* Right cluster */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.4rem' }}>
          {/* Phone pill */}
          {settings.phone && (
            <a href={`tel:${settings.phone}`} style={{
              display: 'flex', alignItems: 'center', gap: '0.55rem',
              background: 'var(--navy)', color: 'white',
              padding: '0.5rem 1.2rem', borderRadius: 9999,
              fontSize: '0.88rem', fontWeight: 600,
              letterSpacing: '0.03em', transition: 'all 0.3s'
            }}
            onMouseEnter={e => e.currentTarget.style.background = 'var(--green2)'}
            onMouseLeave={e => e.currentTarget.style.background = 'var(--navy)'}>
              <i className="fas fa-phone" style={{ color: 'var(--gold)', fontSize: '0.8rem' }} />
              {settings.phone}
            </a>
          )}

          {/* Lang switcher */}
          <div style={{
            display: 'flex', alignItems: 'center',
            background: 'var(--cream)', borderRadius: 9999,
            padding: '3px', gap: '2px',
            border: '1px solid rgba(10,25,60,0.1)'
          }}>
            {['fr', 'en', 'ar'].map(l => (
              <button key={l} onClick={() => { setLang(l); navigate('/') }} style={{
                padding: '0.3rem 0.75rem', borderRadius: 9999,
                fontSize: '0.78rem', fontWeight: 600,
                cursor: 'pointer', border: 'none',
                background: lang === l ? 'var(--navy)' : 'transparent',
                color: lang === l ? 'white' : 'var(--gray)',
                letterSpacing: '0.05em', transition: 'all 0.25s'
              }}>
                {l.toUpperCase()}
              </button>
            ))}
          </div>

          {/* Hamburger */}
          <button onClick={() => setMenuOpen(!menuOpen)} style={{
            display: 'none', background: 'none', border: 'none',
            cursor: 'pointer', flexDirection: 'column', gap: '5px', padding: '4px'
          }} className="hamburger-btn" aria-label="Menu">
            {[0,1,2].map(i => (
              <span key={i} style={{
                display: 'block', width: 24, height: 2,
                background: 'var(--navy)', borderRadius: 2,
                transition: 'all 0.3s'
              }} />
            ))}
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      {menuOpen && (
        <div style={{
          background: 'white', borderTop: '1px solid rgba(10,25,60,0.08)',
          padding: '1rem 1.5rem 1.5rem'
        }}>
          {links.map(l => (
            <Link key={l.to} to={l.to} style={{
              display: 'block', padding: '0.75rem 0',
              borderBottom: '1px solid rgba(10,25,60,0.06)',
              fontWeight: 500, color: isActive(l.to) ? 'var(--green2)' : 'var(--navy)'
            }}>
              {l.label}
            </Link>
          ))}
        </div>
      )}

      <style>{`
        @media (max-width: 768px) {
          .nav-links-desktop { display: none !important; }
          .hamburger-btn { display: flex !important; }
        }
      `}</style>
    </nav>
  )
}
