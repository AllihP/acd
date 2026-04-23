import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  
  // 🔑 CRITIQUE : Préfixe les URLs d'assets avec /static/ pour Django
  base: '/static/',
  
  build: {
    // Sortie relative au dossier frontend (pas de chemin absolu)
    outDir: 'dist',
    assetsDir: 'assets',
    emptyOutDir: true,
    manifest: true,
  },
  
  server: {
    origin: 'http://localhost:5173',
    port: 5173
  }
})