import axios from 'axios'

const BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

const api = axios.create({ baseURL: BASE })

export const fetchAll        = ()       => api.get('/all/')
export const fetchHero       = ()       => api.get('/hero/')
export const fetchAbout      = ()       => api.get('/about/')
export const fetchServices   = ()       => api.get('/services/')
export const fetchWhyItems   = ()       => api.get('/why/')
export const fetchPortfolio  = (cat)    => api.get('/portfolio/' + (cat ? `?category=${cat}` : ''))
export const fetchTestimonials = ()     => api.get('/testimonials/')
export const fetchSettings   = ()       => api.get('/settings/')
export const sendContact     = (data)   => api.post('/contact/', data)

export default api
