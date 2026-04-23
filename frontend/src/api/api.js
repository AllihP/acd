import axios from 'axios'
const BASE = "https://acd-fqjq.onrender.com/api"
const api = axios.create({ baseURL: BASE })

export const fetchAll          = ()      => api.get('/core/all/')
export const fetchHero         = ()      => api.get('/core/hero/')
export const fetchPortfolio    = (cat)   => api.get('/core/portfolio/' + (cat ? `?category=${cat}` : ''))
export const sendContact       = (data)  => api.post('/contact/contact/', data)

export default api