# ACD — Application Web Complète
### Agence de Communication pour le Développement — N'Djamena, Tchad

> **Stack :** Django 4.2 (Backend) + React 18 + Vite (Frontend)  
> **Langues :** Français · English · العربية  
> **Admin :** Jazzmin (design moderne aux couleurs ACD)

---

## 🚀 Démarrage rapide (recommandé)

```bash
# Depuis la racine du projet
bash start.sh
```

Le script va automatiquement :
- Créer l'environnement Python et installer les dépendances
- Lancer les migrations et charger les données initiales
- Créer le superutilisateur admin
- Lancer le backend (port 8000) et le frontend (port 5173)

**Accès rapides :**
| URL | Description |
|-----|-------------|
| http://localhost:5173 | Frontend React |
| http://localhost:8000/admin | Admin Django |
| http://localhost:8000/api/all/ | API principale |

**Identifiants admin par défaut :**
```
Utilisateur : admin
Mot de passe : ACD@admin2025
```
⚠️ *Changez le mot de passe en production !*

---

## 📁 Structure du projet

```
acd_project/
├── start.sh                    # Script de démarrage automatique
├── README.md
│
├── backend/                    # Django REST API
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── acd_backend/
│   │   ├── settings.py         # Config Django + Jazzmin
│   │   └── urls.py
│   ├── apps/
│   │   ├── core/               # Contenu principal du site
│   │   │   ├── models.py       # SiteSettings, HeroSection, AboutSection,
│   │   │   │                   # Service, WhyItem, PortfolioItem, Testimonial
│   │   │   ├── admin.py        # Interface admin stylisée
│   │   │   ├── serializers.py
│   │   │   ├── views.py        # API REST
│   │   │   ├── urls.py
│   │   │   └── fixtures/
│   │   │       └── initial_data.json
│   │   └── contact/            # Formulaire de contact
│   │       ├── models.py       # ContactMessage
│   │       ├── admin.py
│   │       └── ...
│   └── static/
│       └── admin/css/
│           └── custom_admin.css # CSS admin ACD (navy/green/gold)
│
└── frontend/                   # React + Vite
    ├── package.json
    ├── vite.config.js          # Proxy vers Django
    └── src/
        ├── App.jsx             # Router principal + loading screen
        ├── main.jsx
        ├── api/api.js          # Appels Axios vers Django
        ├── context/
        │   └── LangContext.jsx # Gestion FR/EN/AR
        ├── components/
        │   ├── Navbar.jsx      # Navbar sticky + langue + mobile
        │   ├── Topbar.jsx      # Barre supérieure
        │   └── Footer.jsx      # Footer complet
        ├── pages/
        │   ├── Accueil.jsx     # Hero + Ribbon + Services + Why + Testimonials
        │   ├── APropos.jsx     # Histoire + Faits + Valeurs
        │   ├── Realisations.jsx# Portfolio filtrable par catégorie
        │   ├── Projets.jsx     # Services accordéon détaillé
        │   └── Contact.jsx     # Formulaire + validation + coordonnées
        └── styles/
            └── globals.css     # Variables CSS + animations globales
```

---

## 🖥️ Installation manuelle

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate          # Linux/macOS
# ou : venv\Scripts\activate       # Windows

pip install -r requirements.txt
cp .env.example .env               # Editez si besoin

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata apps/core/fixtures/initial_data.json
python manage.py createsuperuser
python manage.py collectstatic
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 📡 API Endpoints

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/all/` | Toutes les données du site |
| GET | `/api/hero/` | Section Hero/Accueil |
| GET | `/api/about/` | Section À propos |
| GET | `/api/services/` | Services/Expertises |
| GET | `/api/why/` | Raisons de nous choisir |
| GET | `/api/portfolio/` | Réalisations (filtre: `?category=branding`) |
| GET | `/api/testimonials/` | Témoignages |
| GET | `/api/settings/` | Paramètres généraux |
| POST | `/api/contact/` | Envoyer un message |

---

## 🎨 Gestion du contenu (Admin Django)

L'interface admin est accessible sur **http://localhost:8000/admin**.

### Ordre de remplissage recommandé :

1. **Paramètres du site** → email, téléphone, adresse, réseaux sociaux
2. **Section Accueil (Hero)** → titre, sous-titre, stats, image de fond
3. **Section À propos** → texte, faits clés, image principale
4. **Services / Expertises** → icônes FontAwesome, titres, descriptions
5. **Raisons / Piliers** → arguments différenciants
6. **Réalisations (Portfolio)** → images, catégories, descriptions
7. **Témoignages** → auteur, rôle, texte, photo, note

### Langues disponibles :
Chaque champ de contenu possède 3 variantes : `_fr`, `_en`, `_ar`.  
Le frontend choisit automatiquement selon la langue sélectionnée par l'utilisateur.

### Catégories Portfolio :
`branding` · `digital` · `evenement` · `print` · `social` · `audiovisuel`

### Icônes FontAwesome pour les services :
```
fas fa-bullhorn      → Communication
fas fa-palette       → Branding
fas fa-globe         → Digital
fas fa-calendar-star → Événementiel
fas fa-mobile-alt    → Social Media
fas fa-video         → Audiovisuel
fas fa-chart-line    → Stratégie
fas fa-print         → Print
```

---

## 🖼️ Ajout d'images

Les images se gèrent depuis l'admin Django :
- **Hero** → Section Accueil → champ "Image de fond"
- **À propos** → Section À propos → champ "Photo principale"
- **Portfolio** → Réalisations → champ "Image principale" *(requis)*
- **Témoignages** → champ "Photo" *(optionnel)*

Les images sont stockées dans `backend/media/` et servies via `/media/`.

---

## 🌍 Multilingue (FR/EN/AR)

- Le switcher de langue se trouve dans la **Navbar** (boutons FR · EN · AR)
- La direction du texte bascule automatiquement en **RTL** pour l'arabe
- La langue est persistée dans `localStorage`

---

## 🔐 Production

```bash
# Changer la clé secrète dans .env
SECRET_KEY=votre-cle-ultra-secrete

# Désactiver le debug
DEBUG=False

# Définir les hôtes autorisés
ALLOWED_HOSTS=votre-domaine.com,www.votre-domaine.com

# Builder le frontend
cd frontend && npm run build

# Les fichiers statiques iront dans backend/staticfiles/
```

---

## 📦 Dépendances principales

### Backend
| Package | Version | Usage |
|---------|---------|-------|
| Django | 4.2 | Framework web |
| djangorestframework | 3.14 | API REST |
| jazzmin | 2.6 | Admin UI moderne |
| django-cors-headers | 4.3 | CORS pour React |
| Pillow | 10.3 | Gestion images |
| django-filter | 23.5 | Filtres API |

### Frontend
| Package | Version | Usage |
|---------|---------|-------|
| React | 18 | UI Framework |
| Vite | 5 | Build tool |
| React Router | 6 | Navigation |
| Axios | 1.7 | Requêtes HTTP |
| react-intersection-observer | 9 | Animations scroll |

---

*© 2025 ACD — Agence de Communication pour le Développement, N'Djamena, Tchad*
