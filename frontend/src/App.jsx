import { useEffect, useState } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import Navbar from './components/Navbar'
import Topbar from './components/Topbar'
import Footer from './components/Footer'
import Accueil from './pages/Accueil'
import APropos from './pages/APropos'
import Realisations from './pages/Realisations'
import Projets from './pages/Projets'
import Contact from './pages/Contact'
import { fetchAll } from './api/api'
import { useLang } from './context/LangContext'

function ScrollToTop() {
  const { pathname } = useLocation()
  useEffect(() => { window.scrollTo(0, 0) }, [pathname])
  return null
}

function LoadingScreen({ hide }) {
  return (
    <div className={`loading-screen${hide ? ' hide' : ''}`}>
      <div style={{ textAlign: 'center' }}>ACD</div>
    </div>
  )
}

export default function App() {
  const { lang } = useLang()
  const [siteData, setSiteData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [hideLoader, setHideLoader] = useState(false)

  useEffect(() => {
    fetchAll()
      .then(r => {
        setSiteData(r.data)
        setHideLoader(true)
        setTimeout(() => setLoading(false), 500)
      })
      .catch(() => {
        setHideLoader(true)
        setTimeout(() => setLoading(false), 500)
      })
  }, [])

  const settings = siteData?.settings || {}

  if (loading) return <LoadingScreen hide={hideLoader} />

  return (
    <>
      <ScrollToTop />
      <Topbar settings={settings} lang={lang} />
      <Navbar settings={settings} lang={lang} />
      
      <Routes>
        <Route path="/" element={<Accueil data={siteData} />} />
        <Route path="/a-propos" element={<APropos data={siteData} />} />
        <Route path="/realisations" element={<Realisations data={siteData} />} />
        <Route path="/projets" element={<Projets data={siteData} />} />
        <Route path="/contact" element={<Contact settings={settings} />} />
        <Route path="*" element={<Accueil data={siteData} />} />
      </Routes>
      
      <Footer settings={settings} lang={lang} />
    </>
  )
}