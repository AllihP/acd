import axios from 'axios'

// L'URL de base doit pointer vers la racine de l'API
const BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

const api = axios.create({ baseURL: BASE })

// Utilisation des préfixes /core/ et /contact/ définis dans urls.py
export const fetchAll        = ()       => api.get('/core/all/')
export const fetchHero       = ()       => api.get('/core/hero/')
export const fetchAbout      = ()       => api.get('/core/about/')
export const fetchServices   = ()       => api.get('/core/services/')
export const fetchWhyItems   = ()       => api.get('/core/why/')
export const fetchPortfolio  = (cat)    => api.get('/core/portfolio/' + (cat ? `?category=${cat}` : ''))
export const fetchTestimonials = ()     => api.get('/core/testimonials/')
export const fetchSettings   = ()       => api.get('/core/settings/')

// Le formulaire de contact est dans l'app contact
export const sendContact     = (data)   => api.get('/contact/contact/', data)

export default api