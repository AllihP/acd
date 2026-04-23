import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  
  // 🔑 CRITIQUE : Préfixe toutes les URLs d'assets avec /static/
  base: '/static/',
  
  build: {
    // Dossier de sortie lu par Django via STATICFILES_DIRS
    outDir: resolve(__dirname, '../backend/frontend/dist'),
    assetsDir: 'assets',
    emptyOutDir: true,
    
    // Génération de manifest pour WhiteNoise
    manifest: true,
    rollupOptions: {
      output: {
        // Hash des fichiers pour le cache
        entryFileNames: 'assets/[name]-[hash].js',
        chunkFileNames: 'assets/[name]-[hash].js',
        assetFileNames: 'assets/[name]-[hash].[ext]'
      }
    }
  },
  
  server: {
    origin: 'http://localhost:5173', // Pour le HMR en dev
    port: 5173
  }
})