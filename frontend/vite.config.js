import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  
  // 🔑 CRITIQUE : Préfixe les assets avec /static/ pour Django
  base: '/static/',
  
  build: {
    outDir: resolve(__dirname, '../backend/frontend/dist'),
    assetsDir: 'assets',
    emptyOutDir: true,
    manifest: true,
    rollupOptions: {
      output: {
        entryFileNames: 'assets/[name]-[hash].js',
        chunkFileNames: 'assets/[name]-[hash].js',
        assetFileNames: 'assets/[name]-[hash].[ext]'
      }
    }
  },
  
  server: {
    origin: 'http://localhost:5173',
    port: 5173
  }
})