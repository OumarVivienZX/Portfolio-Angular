# Portfolio

This project was generated using [Angular CLI](https://github.com/angular/angular-cli) version 21.0.3.

## Development server

To start a local development server, run:

```bash
ng serve
```

Once the server is running, **open the exact URL printed in the terminal**.

Note: if port `4200` is already used, Angular will propose another port (ex: `http://localhost:53916/`).
The application will automatically reload whenever you modify any of the source files.

## Code scaffolding

Angular CLI includes powerful code scaffolding tools. To generate a new component, run:

```bash
ng generate component component-name
```

For a complete list of available schematics (such as `components`, `directives`, or `pipes`), run:

```bash
ng generate --help
```

## Building

To build the project run:

```bash
ng build
```

This will compile your project and store the build artifacts in the `dist/` directory. By default, the production build optimizes your application for performance and speed.

## Running unit tests

To execute unit tests with the [Vitest](https://vitest.dev/) test runner, use the following command:

```bash
ng test
```

## Running end-to-end tests

For end-to-end (e2e) testing, run:

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Consommation de l'API Django

### Authentification / Sécurité

La version actuelle du backend utilise JWT (via `djangorestframework-simplejwt`).
Les écritures (POST/PUT/PATCH/DELETE) requièrent un jeton valide ; les lectures restent ouvertes en lecture seule.

- Pour obtenir un jeton vous pouvez appeler l'endpoint `POST /api/token/` avec un JSON `{ "username": "...", "password": "..." }`.
- Le token est ensuite transmis dans l'en-tête `Authorization: Bearer <token>` (un 
interceptor Angular s'occupe de cela automatiquement si l'utilisateur est connecté).

Côté frontend un composant de connexion (`/login`) permet de récupérer et stocker le
jeton dans `localStorage`. Le `Header` affiche un lien de connexion/déconnexion en
fonction de l'état d'authentification.


Le frontend interagit avec une API Django située dans le dossier `api-django`.
La constante `API_URL` se trouve dans `src/app/shared/config.ts` et pointe vers `environment.apiUrl`.
Par défaut en dev :

```ts
export const API_URL = 'http://localhost:8000/api/';
```

Les services du dossier `src/app/shared/service` offrent des méthodes retournant des
`Observable` typés pour récupérer les données du backend (utilisateur, projets,
expériences, etc.) et envoyer des formulaires de contact.

### Données dynamiques (admin Django)

Les sections du portfolio (profil, projets, services, expériences, réseaux sociaux, localisation)
proviennent de l’API Django et peuvent être modifiées via l’interface d’admin :
- Admin: `http://localhost:8000/admin/`
- API: `http://localhost:8000/api/`

Les lectures (GET) sont **publiques**. Les écritures (POST/PUT/PATCH/DELETE) sont **réservées aux admins/staff**.

### Étapes pour démarrer le backend

1. Aller dans `api-django` :
   ```bash
   cd api-django
   python -m venv .venv   # optionnel
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```
2. L'API sera disponible sur `http://localhost:8000/api/`.

### Dépannage rapide (si “je ne vois pas les infos”)

- Vérifie que **Django tourne** sur `http://localhost:8000/` et que l’API répond sur `http://localhost:8000/api/Utilisateur/1/`.
- Vérifie que tu utilises **le bon port Angular** (celui affiché par `ng serve`).
- CORS: le backend autorise `localhost` sur n’importe quel port en dev (cf. `api-django/portfolio_api/settings.py`).

### Frontend

1. Démarrer l'application Angular :
   ```bash
   npm install
   npm run start
   ```
2. Le composant `Introduction` montre un exemple d'appel à `UserService.getUserById(1)`
et met à jour l'interface via une `signal`.

## Déploiement (Netlify) + formulaire de contact

### Pré-requis
- Le **frontend** est déployé sur Netlify (site statique).
- Le **backend Django** doit être déployé ailleurs (Render / Railway / Fly.io / VPS, etc.).

### 1) Déployer le backend Django
- Déployer le dossier `api-django/` sur une plateforme Python.
- Configurer les variables d’environnement: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`, `EMAIL_*`.
- Lancer `python manage.py migrate` et créer un admin (`createsuperuser`).

### 2) Pointer Angular vers l’API en production
Dans `src/environments/environment.prod.ts`, mettre :
`apiUrl: 'https://TON_BACKEND/api/'`

### 3) Garder le formulaire de contact fonctionnel
Option recommandée (simple) :
- Le formulaire Angular fait un `POST` vers `POST /api/PriseDeContact/` (autorisé anonymement).
- Le backend enregistre le message et peut envoyer un email via SMTP (config `.env`).

Alternative (si tu ne veux pas déployer Django) :
- Utiliser une Netlify Function (serverless) + SendGrid/Mailgun pour envoyer l’email.
  Dans ce cas on remplacera l’appel API Django par un appel `/.netlify/functions/contact`.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
