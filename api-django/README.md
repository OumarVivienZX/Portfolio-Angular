# API Django - Portfolio

Backend REST API pour le portfolio personnel de **KONAN OUMAR VIVIEN**.

Construit avec **Django 5.1** et **Django REST Framework**.

---

## 🚀 Démarrage rapide

### 1. Installation

```bash
cd api-django

# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Configuration

Copier `.env.example` en `.env` et remplir les valeurs :

```bash
cp .env.example .env
```

Configuration par défaut (développement) :
```
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 3. Migrations & Démarrage

```bash
# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

L'API est disponible sur **`http://localhost:8000/api/`**

Admin panel : **`http://localhost:8000/admin/`**

> Note frontend: `ng serve` peut démarrer sur un port différent de 4200 si ce port est occupé.
> Le backend est configuré pour autoriser `http://localhost:<port>` en dev (CORS).

---

## 📁 Structure

```
api-django/
├── portfolio/                 # App principale
│   ├── models.py             # Modèles (Utilisateur, Projet, Experience, etc.)
│   ├── serializers.py        # Sérialiseurs DRF
│   ├── viewsets.py           # ViewSets REST
│   ├── migrations/           # Migrations de base de données
│   └── api/
│       └── urls.py           # Routage API
├── portfolio_api/            # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env.example              # Template des variables d'environnement
├── manage.py
├── requirements.txt
└── db.sqlite3               # Base de données (git-ignored)
```

---

## 📊 Modèles & API

### Modèles
- **Utilisateur** : Informations de profil (nom, email, cv, etc.)
- **Projet** : Projets réalisés
- **Experience** : Expériences professionnelles
- **Service** : Services proposés
- **PriseDeContact** : Messages de contact
- **ReseauSocial** : Réseaux sociaux
- **Localisation** : Localisation géographique

### Endpoints

```
GET/POST    /api/Utilisateur/
GET         /api/Utilisateur/{id}/
GET         /api/Projet/?utilisateur=1
GET         /api/Experience/?utilisateur=1
GET         /api/Service/?utilisateur=1
POST        /api/PriseDeContact/
GET         /api/ReseauSocial/?utilisateur=1
GET         /api/Localisation/?utilisateur=1
```

Admin panel complet avec filtrages disponible sur `/admin/`.

---

## 🔐 Configuration de sécurité

### Variables d'environnement requises

En développement :
- `.env` peut être en SQLite local
- DEBUG=True autorisé

En production :
- ✅ Utiliser PostgreSQL
- ✅ DEBUG=False obligatoire
- ✅ SECRET_KEY unique et sécurisée
- ✅ ALLOWED_HOSTS=votre-domaine.com
- ✅ HTTPS obligatoire

---

## 📧 Configuration des mails

Pour que les formulaires de contact fonctionnent :

### Avec Gmail
1. Activer l'authentification à 2 facteurs sur Gmail
2. Générer un **"mot de passe d'application"** dans les paramètres Google
3. Remplir dans `.env` :
   ```
   EMAIL_HOST_USER=votre-email@gmail.com
   EMAIL_HOST_PASSWORD=votre-mot-de-passe-app
   ```

### Avec un serveur SMTP personnalisé
Adapter les paramètres dans `.env` :
```
EMAIL_HOST=votre-smtp.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

---

## ⚙️ Commandes utiles

```bash
# Créer un superutilisateur
python manage.py createsuperuser

# Lancer les migrations
python manage.py migrate

# Créer une nouvelle migration
python manage.py makemigrations

# Shell Django (interactive)
python manage.py shell

# Collecter les fichiers statiques (production)
python manage.py collectstatic

# Tests
python manage.py test
```

---

## 🚢 Déploiement en production

### Checklist
- [ ] `.env` créé avec les paramètres de production
- [ ] DEBUG=False
- [ ] ALLOWED_HOSTS configuré
- [ ] CORS_ALLOWED_ORIGINS pointant vers le domaine Angular
- [ ] Base de données : PostgreSQL ou MySQL
- [ ] Certificat SSL/HTTPS
- [ ] Variables d'environnement sécurisées

### Déploiement avec un frontend Netlify

Si le frontend Angular est déployé sur Netlify, tu dois :
- Déployer l’API Django sur un domaine public (Render / Railway / Fly.io / VPS, etc.)
- Mettre `CORS_ALLOWED_ORIGINS` sur l’URL Netlify (ex: `https://mon-portfolio.netlify.app`)
- (Optionnel) Garder `CORS_ALLOWED_ORIGIN_REGEXES` seulement en dev (localhost).
- Garder `POST /api/PriseDeContact/` ouvert (anonyme) pour le formulaire de contact
- Configurer SMTP (`EMAIL_HOST_*`) pour recevoir les messages

Dans Angular (prod), configure `apiUrl` sur `https://<ton-backend>/api/`.

### Exemple de déploiement (Heroku, PythonAnywhere, etc.)
1. Créer un `.env` avec SECRET_KEY unique
2. Configurer les variables d'environnement dans la plateforme
3. Lancer les migrations : `python manage.py migrate`
4. Créer un superutilisateur en production si besoin

---

## 📝 Notes

- ✅ `.env.example` est versionné (pour référence)
- ❌ `.env` n'est JAMAIS commité (contient secrets)
- Les mails en production nécessitent un `.env` valide
- Admin panel permet la gestion complète des données

Pour la documentation Django : [docs.djangoproject.com](https://docs.djangoproject.com/)
