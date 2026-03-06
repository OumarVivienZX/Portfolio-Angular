# Portfolio Angular + Django REST

Portfolio personnel de **KONAN OUMAR VIVIEN** construit avec **Angular 21** et **Django REST Framework**.

## 🚀 Démarrage rapide

### Prérequis
- **Node.js** 18+ et npm
- **Python** 3.9+
- **Git**

### Installation & Lancement

#### 1. Frontend (Angular)

```bash
# À la racine du projet
npm install
npm run start
```
- Application disponible sur **`http://localhost:4200/`**

#### 2. Backend (Django)

```bash
cd api-django

# Créer l'environnement virtuel
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt

# Migrations et démarrage
python manage.py migrate
python manage.py runserver
```
- API disponible sur **`http://localhost:8000/api/`**

### Configuration des variables d'environnement (Backend)

Dupliquer `.env.example` en `.env` et remplir les valeurs :
```bash
cp .env.example .env
```

⚠️ **Important** : Le fichier `.env` contient des secrets (clés API, mots de passe mails).
Ne jamais le commiter au dépôt !

---

## 📁 Architecture

```
portfolio-angular/
├── src/
│   ├── app/
│   │   ├── home/                 # Composants des différentes sections
│   │   ├── shared/
│   │   │   ├── models/           # Interfaces TypeScript (IUser, IProject, etc.)
│   │   │   ├── service/          # Services HTTP (UserService, ProjectService, etc.)
│   │   │   ├── base/             # BaseService pour les requêtes HTTP
│   │   │   └── config.ts         # Configuration API (API_URL)
│   │   └── app.config.ts         # Configuration Angular
│   └── assets/                   # Images, CSS, JS
├── api-django/
│   ├── portfolio/                # App Django
│   │   ├── models.py             # Modèles (Utilisateur, Projet, Expérience, etc.)
│   │   ├── serializers.py        # Sérialiseurs DRF
│   │   ├── viewsets.py           # ViewSets REST
│   │   └── api/                  # Routes API
│   ├── portfolio_api/            # Configuration Django
│   ├── manage.py
│   ├── .env.example              # Template des variables d'environnement
│   └── requirements.txt
└── README.md
```

---

## 🔗 API Endpoints

### Base URL
```
http://localhost:8000/api/
```

### Ressources principales
| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/Utilisateur/` | GET | Lister tous les utilisateurs |
| `/Utilisateur/{id}/` | GET | Récupérer un utilisateur |
| `/Projet/?utilisateur=1` | GET | Projets d'un utilisateur |
| `/Experience/?utilisateur=1` | GET | Expériences d'un utilisateur |
| `/Service/?utilisateur=1` | GET | Services d'un utilisateur |
| `/PriseDeContact/` | POST | Soumettre un message de contact |
| `/ReseauSocial/?utilisateur=1` | GET | Réseaux sociaux |
| `/Localisation/?utilisateur=1` | GET | Localisation |

---

## 🛠 Développement

### Scripts utiles

**Frontend** :
```bash
npm run build    # Build pour production
npm run test     # Lancer les tests
```

**Backend** :
```bash
python manage.py createsuperuser  # Créer admin
python manage.py runserver        # Lancer le serveur
```

Admin panel : **`http://localhost:8000/admin/`**

---

## 📊 Stack Technique

### Frontend
- **Angular 21** (Standalone Components)
- **TypeScript** 5.9
- **RxJS** 7.8
- **Bootstrap 5**

### Backend
- **Django** 5.1
- **Django REST Framework**
- **SQLite** (développement)

---

## 🚢 Déploiement

### Points importants
1. **Variables d'environnement** : Créer un fichier `.env` en production (jamais le commiter)
2. **ALLOWED_HOSTS** : Configurer le domaine de production dans `settings.py`
3. **CORS** : Ajuster les origines autorisées dans Django
4. **Base de données** : Utiliser PostgreSQL en production
5. **Secrets** : Changer la `SECRET_KEY` Django et les mots de passe

### Stratégie `.env`

- ✅ `.env.example` est commité (contient les clés sans valeurs)
- ❌ `.env` ne doit JAMAIS être commité (contient les secrets)
- En production, créer manuellement un `.env` avec les vraies valeurs

---

## 📝 Notes

- Le composant `Introduction` charge et affiche les données utilisateur via Signals Angular
- Tous les services utilisent des `Observable` typés
- HTTPS recommandé en production
- Les mails en production nécessitent un `.env` correctement configuré

Pour plus d'informations : [angular.dev](https://angular.dev) | [django.palletsprojects.com](https://www.djangoproject.com/)
