import { Link } from 'react-router-dom'
import { useLang } from '../context/LangContext'

export default function Footer({ settings }) {
  const { lang, ui } = useLang()
  const addr = settings[`address_${lang}`] || settings.address_fr || "Agence Internationale"
  
  const navLinks = [
    { to: '/', label: ui.nav_home },
    { to: '/a-propos', label: ui.nav_about },
    { to: '/realisations', label: ui.nav_realisations },
    { to: '/projets', label: ui.nav_projets },
    { to: '/contact', label: ui.nav_contact },
  ]

  return (
    <footer style={{ background: 'var(--navy)', color: 'rgba(255,255,255,0.7)', paddingTop: '5rem' }}>
      <div className="responsive-grid-footer" style={{ maxWidth: 1440, margin: '0 auto', padding: '0 3rem 4rem' }}>
        <div style={{ fontFamily: "'Cormorant Garamond',serif", fontSize: '2rem', fontWeight: 700, color: 'var(--gold)', marginBottom: '1.2rem', letterSpacing: '0.06em' }}>
          ACD
          <p style={{ fontSize: '0.9rem', lineHeight: 1.7, maxWidth: 320, marginBottom: '2rem' }}>{ui.footer_desc}</p>
          <div style={{ display: 'flex', gap: '1rem' }}>
            {settings.facebook && <SocialIcon href={settings.facebook} icon="fab fa-facebook-f" />}
            {settings.linkedin && <SocialIcon href={settings.linkedin} icon="fab fa-linkedin-in" />}
            {settings.instagram && <SocialIcon href={settings.instagram} icon="fab fa-instagram" />}
            {settings.twitter && <SocialIcon href={settings.twitter} icon="fab fa-x-twitter" />}
            {settings.youtube && <SocialIcon href={settings.youtube} icon="fab fa-youtube" />}
          </div>
        </div>

        <div>
          <h4 style={{ color: 'white', fontWeight: 700, fontSize: '0.85rem', letterSpacing: '0.12em', textTransform: 'uppercase', marginBottom: '1.5rem' }}>{ui.footer_nav}</h4>
          <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {navLinks.map(l => (
              <li key={l.to}>
                <Link to={l.to} style={{ fontSize: '0.9rem', transition: 'color 0.25s' }}
                  onMouseEnter={e => e.currentTarget.style.color = 'var(--green)'}
                  onMouseLeave={e => e.currentTarget.style.color = 'rgba(255,255,255,0.7)'}>
                  {l.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <h4 style={{ color: 'white', fontWeight: 700, fontSize: '0.85rem', letterSpacing: '0.12em', textTransform: 'uppercase', marginBottom: '1.5rem' }}>{ui.footer_services}</h4>
          <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {(ui.service_options || []).slice(0, 6).map(s => (
              <li key={s.value} style={{ fontSize: '0.9rem' }}>{s.label}</li>
            ))}
          </ul>
        </div>

        <div>
          <h4 style={{ color: 'white', fontWeight: 700, fontSize: '0.85rem', letterSpacing: '0.12em', textTransform: 'uppercase', marginBottom: '1.5rem' }}>{ui.footer_contact}</h4>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {addr && (
              <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'flex-start' }}>
                <i className="fas fa-map-marker-alt" style={{ color: 'var(--gold)', marginTop: '0.2rem', flexShrink: 0 }} />
                <span style={{ fontSize: '0.9rem' }}>{addr}</span>
              </div>
            )}
            {settings.phone && (
              <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center' }}>
                <i className="fas fa-phone" style={{ color: 'var(--gold)', flexShrink: 0 }} />
                <a href={`tel:${settings.phone}`} style={{ fontSize: '0.9rem', color: 'var(--gold)', fontWeight: 600 }}>{settings.phone}</a>
              </div>
            )}
            {settings.email && (
              <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center' }}>
                <i className="fas fa-envelope" style={{ color: 'var(--gold)', flexShrink: 0 }} />
                <a href={`mailto:${settings.email}`} style={{ fontSize: '0.9rem', color: 'rgba(255,255,255,0.7)' }}>{settings.email}</a>
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="footer-bottom-flex" style={{ borderTop: '1px solid rgba(255,255,255,0.08)', padding: '1.5rem 3rem', maxWidth: 1440, margin: '0 auto' }}>
        <p style={{ fontSize: '0.82rem' }}>{ui.copy}</p>
        <p style={{ fontSize: '0.82rem', color: 'rgba(255,255,255,0.4)' }}>Made with <span style={{ color: 'var(--green)' }}>♥</span> Worldwide</p>
      </div>
    </footer>
  )
}

function SocialIcon({ href, icon }) {
  return (
    <a href={href} target="_blank" rel="noreferrer" style={{
      width: 40, height: 40, borderRadius: 10, background: 'rgba(255,255,255,0.07)',
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      color: 'rgba(255,255,255,0.7)', fontSize: '0.95rem', transition: 'all 0.25s'
    }}
    onMouseEnter={e => { e.currentTarget.style.background = 'var(--green)'; e.currentTarget.style.color = 'white' }}
    onMouseLeave={e => { e.currentTarget.style.background = 'rgba(255,255,255,0.07)'; e.currentTarget.style.color = 'rgba(255,255,255,0.7)' }}>
      <i className={icon} />
    </a>
  )
}