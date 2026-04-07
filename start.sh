#!/bin/bash
# ═══════════════════════════════════════════════════════════════
#  ACD — Script de démarrage rapide
#  Usage : bash start.sh
# ═══════════════════════════════════════════════════════════════

set -e
GREEN='\033[0;32m'; GOLD='\033[0;33m'; BLUE='\033[0;34m'; NC='\033[0m'
BOLD='\033[1m'

echo ""
echo -e "${GOLD}${BOLD}╔══════════════════════════════════════════════╗${NC}"
echo -e "${GOLD}${BOLD}║     ACD — Démarrage de l'application         ║${NC}"
echo -e "${GOLD}${BOLD}╚══════════════════════════════════════════════╝${NC}"
echo ""

# ── BACKEND ────────────────────────────────────────────────────
echo -e "${BLUE}▶ Configuration du backend Django...${NC}"
cd backend

# Copier .env si inexistant
if [ ! -f .env ]; then
  cp .env.example .env
  echo -e "${GREEN}✓ Fichier .env créé${NC}"
fi

# Venv Python
if [ ! -d venv ]; then
  echo -e "${BLUE}  → Création de l'environnement virtuel...${NC}"
  python3 -m venv venv
fi
source venv/bin/activate

echo -e "${BLUE}  → Installation des dépendances Python...${NC}"
pip install -q -r requirements.txt

echo -e "${BLUE}  → Migrations...${NC}"
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# Charger les fixtures initiales
echo -e "${BLUE}  → Chargement des données initiales...${NC}"
python manage.py loaddata apps/core/fixtures/initial_data.json 2>/dev/null || echo "  (fixtures déjà chargées ou ignorées)"

# Collecte des fichiers statiques
python manage.py collectstatic --no-input -v 0

# Créer superuser si non existant
echo -e "${BLUE}  → Vérification du superutilisateur...${NC}"
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@acd-tchad.com', 'ACD@admin2025')
    print('Superuser créé : admin / ACD@admin2025')
else:
    print('Superuser existe déjà.')
"

echo -e "${GREEN}✓ Backend prêt !${NC}"
echo ""

# ── FRONTEND ───────────────────────────────────────────────────
cd ../frontend
echo -e "${BLUE}▶ Installation des dépendances frontend...${NC}"
npm install --silent
echo -e "${GREEN}✓ Frontend prêt !${NC}"
echo ""

# ── LANCEMENT ──────────────────────────────────────────────────
echo -e "${GOLD}${BOLD}╔══════════════════════════════════════════════╗${NC}"
echo -e "${GOLD}${BOLD}║  Lancement des serveurs en parallèle...      ║${NC}"
echo -e "${GOLD}${BOLD}╚══════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  🖥  Backend Django  → ${GREEN}http://localhost:8000${NC}"
echo -e "  ⚡  Admin Django    → ${GREEN}http://localhost:8000/admin${NC}"
echo -e "     Identifiants   : admin / ACD@admin2025"
echo -e "  🌐  Frontend React  → ${GREEN}http://localhost:5173${NC}"
echo ""
echo -e "  Appuyez sur ${BOLD}Ctrl+C${NC} pour arrêter les serveurs."
echo ""

# Démarrage en parallèle
cd ../backend
source venv/bin/activate
python manage.py runserver &
BACKEND_PID=$!

cd ../frontend
npm run dev &
FRONTEND_PID=$!

# Attendre Ctrl+C
trap "echo ''; echo 'Arrêt...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit 0" INT
wait
