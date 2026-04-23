# render.yaml
services:
  - type: web
    name: acd-backend
    env: python
    buildCommand: ./backend/build.sh
    startCommand: gunicorn --chdir backend acd_backend.wsgi:application --bind 0.0.0.0:$PORT --workers 1 --timeout 120
    envVars:
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: false
      - key: ALLOWED_HOSTS
        value: acd-fqjq.onrender.com,localhost,127.0.0.1
      - key: DATABASE_URL
        sync: false  # À définir manuellement dans le dashboard pour sécurité
      - key: PORT
        value: 10000