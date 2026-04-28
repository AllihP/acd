import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
const BASE = `${API_URL}/api`
const MEDIA_BASE = API_URL

const api = axios.create({
  baseURL: BASE,
  withCredentials: true,
})

// ✅ Interceptor CSRF Django
api.interceptors.request.use(config => {
  const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken='))?.split('=')[1]
  if (csrfToken) {
    config.headers['X-CSRFToken'] = csrfToken
  }
  return config
})

// ✅ Helper pour préfixer les URLs d'images venant de l'API
export const withMediaBase = (url) => {
  if (!url) return ''
  if (url.startsWith('http')) return url
  return `${MEDIA_BASE}${url}`
}

export const fetchAll        = () => api.get('/core/all/')
export const fetchHero       = () => api.get('/core/hero/')
export const fetchPortfolio  = (cat) => api.get('/core/portfolio/' + (cat ? `?category=${cat}` : ''))
export const sendContact     = (data) => api.post('/contact/contact/', data)

export default api