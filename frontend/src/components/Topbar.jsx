import { useLang } from '../context/LangContext'

export default function Topbar({ settings }) {
  const { lang, ui } = useLang()

  const topbarText = settings[`topbar_${lang}`] || settings.topbar_fr || 'ACD — Agence de Communication'

  return (
    <div style={{
      background: 'var(--navy)', color: 'rgba(255,255,255,0.75)',
      fontSize: '0.85rem', padding: '0.55rem 3rem',
      display: 'flex', justifyContent: 'space-between', alignItems: 'center',
      letterSpacing: '0.03em'
    }}>
      <span>{topbarText}</span>
      <div style={{ display: 'flex', alignItems: 'center', gap: '2rem' }}>
        {settings.email && (
          <a href={`mailto:${settings.email}`}
             style={{ color: 'var(--gold)', fontWeight: 600 }}>
            <i className="fas fa-envelope" style={{ marginRight: '0.4rem' }} />
            {settings.email}
          </a>
        )}
        <div style={{ display: 'flex', gap: '1rem' }}>
          {settings.facebook  && <a href={settings.facebook}  target="_blank" rel="noreferrer" style={{ color: 'rgba(255,255,255,0.6)' }}><i className="fab fa-facebook-f" /></a>}
          {settings.linkedin  && <a href={settings.linkedin}  target="_blank" rel="noreferrer" style={{ color: 'rgba(255,255,255,0.6)' }}><i className="fab fa-linkedin-in" /></a>}
          {settings.instagram && <a href={settings.instagram} target="_blank" rel="noreferrer" style={{ color: 'rgba(255,255,255,0.6)' }}><i className="fab fa-instagram" /></a>}
          {settings.twitter   && <a href={settings.twitter}   target="_blank" rel="noreferrer" style={{ color: 'rgba(255,255,255,0.6)' }}><i className="fab fa-x-twitter" /></a>}
        </div>
      </div>
    </div>
  )
}
