import axios from 'axios'

// ✅ URL relative en prod pour éviter les erreurs CORS preflight
const BASE = import.meta.env.PROD ? '/api' : 'https://acd-fqjq.onrender.com/api'

const api = axios.create({
  baseURL: BASE,
  withCredentials: true, // Indispensable pour envoyer/recevoir le cookie CSRF
})

// ✅ Interceptor CSRF Django
api.interceptors.request.use(config => {
  const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken='))?.split('=')[1]
  if (csrfToken) {
    config.headers['X-CSRFToken'] = csrfToken
  }
  return config
})

export const fetchAll        = () => api.get('/core/all/')
export const fetchHero       = () => api.get('/core/hero/')
export const fetchPortfolio  = (cat) => api.get('/core/portfolio/' + (cat ? `?category=${cat}` : ''))
export const sendContact     = (data) => api.post('/contact/contact/', data)

export default api