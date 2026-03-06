# Rapport d'audit — API Django & Frontend Angular

**Projet :** Portfolio Angular  
**Objectif :** Vérifier que l’API Django communique correctement avec le frontend Angular et documenter l’architecture.

---

## ÉTAPE 1 — Analyse globale du projet

### Structure globale

Le dépôt contient **deux applications** dans un même workspace :

- **Frontend Angular** (racine du projet) : application SPA (Single Page Application).
- **Backend Django** (dossier `api-django/`) : API REST pour les données du portfolio.

```
portfolio-angular/
├── src/                    # Source Angular
│   ├── app/
│   │   ├── home/            # Page d'accueil et sections (about, contact, projet, etc.)
│   │   ├── shared/          # Partagé : services, modèles, composants, config
│   │   │   ├── base/        # BaseService (appels HTTP)
│   │   │   ├── models/      # Interfaces TypeScript (IUser, IProject, etc.)
│   │   │   └── service/     # Services métier (UserService, ContactService, etc.)
│   │   ├── app.config.ts    # Configuration app (Router, HttpClient)
│   │   └── app.routes.ts
│   └── environments/        # environment.ts / environment.prod.ts (API_URL)
├── api-django/              # Backend Django
│   ├── portfolio/           # App Django "portfolio"
│   │   ├── models.py        # Utilisateur, Projet, Experience, Service, PriseDeContact, etc.
│   │   ├── serializers.py   # DRF serializers
│   │   ├── viewsets.py      # ViewSets REST
│   │   └── api/urls.py      # Routes /api/...
│   └── portfolio_api/       # Projet Django
│       ├── settings.py      # CORS, INSTALLED_APPS
│       └── urls.py          # Racine : '', admin/, api/
├── angular.json
└── package.json
```

### Dossiers importants

| Dossier / Fichier | Rôle |
|-------------------|------|
| `src/app/shared/service/` | Services Angular qui appellent l’API (UserService, ContactService, etc.). |
| `src/app/shared/base/BaseService.ts` | Service de base : `get<T>`, `save<T>`, `put`, `patch`, `delete`. |
| `src/app/shared/config.ts` | Expose `API_URL` (importe depuis `environments`). |
| `src/app/shared/models/` | Interfaces TypeScript alignées sur les modèles Django. |
| `api-django/portfolio/` | Modèles, serializers, viewsets et routes API. |
| `api-django/portfolio_api/settings.py` | CORS, `ALLOWED_HOSTS`, configuration Django. |

### Organisation du frontend Angular

- **Pages :** une route principale `''` → `Home`, qui regroupe les sections (Introduction, About, Services, Projet, Resume, Contact, etc.).
- **Services :** un service par ressource API (User, Project, Experience, Service/Offer, Contact, Social, Location), tous basés sur `BaseService` et `API_URL`.
- **Modèles :** interfaces dans `shared/models/` (IUser, IProject, IContact, etc.) pour typer les données reçues de l’API.

### Organisation du backend Django

- **Modèles :** `Utilisateur`, `Projet`, `Experience`, `Service`, `PriseDeContact`, `ReseauSocial`, `Localisation`.
- **API :** Django REST Framework avec ViewSets et DefaultRouter.
- **Routes :** préfixe `/api/` puis ressources au pluriel/nom du ViewSet (ex. `Utilisateur`, `Projet`, `PriseDeContact`).

### Flux complet

```
Backend Django
    → Modèles (BDD) → Serializers (JSON) → ViewSets (CRUD)
    → URLs /api/Utilisateur/, /api/Projet/, etc.

API REST (HTTP GET/POST/PUT/DELETE sur ces URLs)

Angular
    → BaseService (HttpClient) : get<T>(), save<T>(), put(), patch(), delete()
    → Services métier (UserService, ContactService, etc.) : appellent BaseService avec API_URL + chemin
    → Composants : injectent les services, .subscribe() ou async pipe
    → Templates : affichent les données (signals, variables)
```

En résumé : **Django expose des endpoints REST ; Angular consomme ces endpoints via des services qui s’appuient sur un BaseService et HttpClient.**

---

## ÉTAPE 2 — Vérification de l’API Django

### Modèles Django

- **Utilisateur :** nom, prénom, photo_profil, description, age, email, lien, cv, telephone.
- **Projet :** utilisateur (FK), resume, image, lien.
- **Experience :** utilisateur (FK), date_debut, date_fin, role, nom_entreprise, description, type_de_contrat.
- **Service :** utilisateur (FK), details, type_de_service, outils.
- **PriseDeContact :** utilisateur (FK), nom, objet, message, **email** (corrigé : était `Email = models.EmailField` sans `()`).
- **ReseauSocial :** utilisateur (FK), nom_platform, lien.
- **Localisation :** utilisateur (FK), pays, ville, **latitude**, **quartier** (corrigé : `lattitde` → `latitude`, `Quartier` → `quartier`).

### Serializers

Tous les modèles ont un `ModelSerializer` avec `fields = '__all__'`. Les champs exposés en JSON correspondent donc aux champs des modèles (y compris `email` pour PriseDeContact et `latitude` / `quartier` pour Localisation).

### Views / ViewSets

- **views.py :** une vue d’accueil `api_home` (message de bienvenue + liste d’endpoints).
- **viewsets.py :** un `ModelViewSet` par ressource. Pour **Projet, Experience, Service, PriseDeContact, ReseauSocial, Localisation**, un **filtrage par `utilisateur`** a été ajouté via `get_queryset()` et le paramètre de requête `?utilisateur=<id>`.

### Routes API (urls.py)

- **Racine projet** (`portfolio_api/urls.py`) : `''` → api_home, `admin/`, `api/` → `portfolio.api.urls`.
- **API** (`portfolio/api/urls.py`) : DefaultRouter enregistre :
  - `Utilisateur` → `/api/Utilisateur/` (liste), `/api/Utilisateur/<id>/` (détail)
  - `Projet` → `/api/Projet/`, `/api/Projet/<id>/`
  - `Experience` → `/api/Experience/`, `/api/Experience/<id>/`
  - `Service` → `/api/Service/`, `/api/Service/<id>/`
  - `PriseDeContact` → `/api/PriseDeContact/`, `/api/PriseDeContact/<id>/`
  - `ReseauSocial` → `/api/ReseauSocial/`, `/api/ReseauSocial/<id>/`
  - `Localisation` → `/api/Localisation/`, `/api/Localisation/<id>/`

### Endpoints utilisés par le frontend

| Service Angular | Endpoint appelé | Méthode |
|-----------------|-----------------|--------|
| UserService | `GET /api/Utilisateur/<id>/` | GET |
| ProjectService | `GET /api/Projet/?utilisateur=<id>` | GET |
| ExperienceService | `GET /api/Experience/?utilisateur=<id>` | GET |
| OfferService | `GET /api/Service/?utilisateur=<id>` | GET |
| ContactService | `GET /api/PriseDeContact/?utilisateur=<id>` | GET |
| ContactService | `POST /api/PriseDeContact/` | POST |
| SocialService | `GET /api/ReseauSocial/?utilisateur=<id>` | GET |
| LocationService | `GET /api/Localisation/?utilisateur=<id>` | GET |

Toutes ces routes existent et sont cohérentes avec le backend après ajout du filtrage `?utilisateur=` et corrections des modèles.

---

## ÉTAPE 3 — Vérification de la communication API

- **URL de base :** définie dans `src/app/shared/config.ts`, qui importe `environment.apiUrl` (`http://localhost:8000/api/` en dev, configurable en prod).
- **Requêtes :** les services concatènent `API_URL` + chemin (ex. `Utilisateur/1/`, `Projet/?utilisateur=1`). Méthodes HTTP utilisées : GET et POST (save) ; BaseService propose aussi put, patch, delete pour d’éventuels usages futurs.
- **CORS :** `django-cors-headers` est activé dans `settings.py` avec `CORS_ALLOWED_ORIGINS` pour `http://localhost:4200` et `http://127.0.0.1:4200`.
- **ALLOWED_HOSTS :** contient `localhost` et `127.0.0.1` pour le dev.

Les données envoyées (ex. IContact pour POST PriseDeContact) correspondent aux champs des serializers (nom, objet, message, email, utilisateur).

---

## ÉTAPE 4 — Vérification du frontend Angular

- **app.config.ts :** `provideHttpClient()` est présent ; HttpClient est donc disponible pour l’injection.
- **URL API :** gérée via `config.ts` → `environments/environment.ts` (dev) et `environment.prod.ts` (prod), avec remplacement de fichier en build production dans `angular.json`.
- **Services :** chaque ressource a son service dans `shared/service/`, qui utilise `BaseService` et les interfaces dans `shared/models/`.
- **Typage :** les retours des services sont typés en `Observable<T>` (ex. `Observable<IUser>`, `Observable<IProject[]>`).
- **HttpClient :** utilisé uniquement dans `BaseService` ; les composants passent par les services métier, ce qui garde la logique API centralisée et testable.
- **Observable :** utilisé pour toute requête HTTP (asynchrone) ; les composants font `.subscribe()` ou peuvent utiliser l’`async` pipe dans les templates.

Aucune mauvaise pratique bloquante ; améliorations apportées : gestion d’erreur dans Introduction, formulaire de contact branché sur l’API, `takeUntilDestroyed` pour éviter les fuites de souscriptions.

---

## ÉTAPE 5 — Vérification du BaseService

### Rôle

- Centraliser les appels HTTP (GET, POST, PUT, PATCH, DELETE) avec un typage générique `T`.
- Éviter de dupliquer `this.http.get/post/...` dans chaque service métier.

### Utilisation par les autres services

Chaque service métier injecte `BaseService` et appelle par exemple :

- `this.baseService.get<IUser>(url)` pour un utilisateur ;
- `this.baseService.get<IProject[]>(url)` pour une liste ;
- `this.baseService.save<IContact>(url, data)` pour créer un contact.

### Méthodes et typage

- `get<T>(url): Observable<T>`
- `save<T>(url, data): Observable<T>` (POST)
- `put<T>(url, data): Observable<T>`
- `patch<T>(url, data): Observable<T>`
- `delete<T>(url): Observable<T>`

Le typage est correct ; `save` accepte `Partial<T>` pour permettre d’envoyer un sous-ensemble des champs si besoin.

### Gestion des erreurs

Les erreurs HTTP remontent dans l’Observable ; les composants les gèrent dans le callback `error` de `.subscribe()` (ex. formulaire de contact). Une évolution possible serait d’ajouter un intercepteur HTTP global pour logs ou messages utilisateur.

---

## ÉTAPE 6 — Vérification des services métiers

Tous les services dans `shared/service/` :

- Utilisent `inject(BaseService)` et `API_URL` depuis `config`.
- Appellent les bons endpoints (noms et query params `utilisateur` conformes au backend).
- Retournent des `Observable<T>` ou `Observable<T[]>` avec les interfaces correspondantes.

Aucune refactorisation structurelle nécessaire ; la cohérence avec l’API Django est assurée.

---

## ÉTAPE 7 — Vérification des composants Angular

- **Introduction :** charge l’utilisateur via `UserService.getUserById(1)`, affiche nom/prénom/description, utilise `takeUntilDestroyed()` et gère l’erreur.
- **Contact :** formulaire relié à `ContactService.sendMessage()` ; champs liés avec `ngModel`, message de succès/erreur et désactivation du bouton pendant l’envoi.
- **Services (section “What I Do”) :** pour l’instant contenu statique ; `OfferService` est injecté mais non utilisé ; on peut plus tard charger les services depuis l’API et les afficher.
- **Projet, Resume, About :** pas encore branchés sur l’API ; les services existants (ProjectService, ExperienceService, etc.) peuvent être utilisés de la même façon que dans Introduction pour afficher projets, expériences, etc.

Recommandation : utiliser `async` pipe dans les templates quand c’est possible pour limiter les souscriptions manuelles et les fuites mémoire.

---

## ÉTAPE 8 — Vérification pour la production

- **Environnements Angular :** `src/environments/environment.ts` (dev) et `environment.prod.ts` (prod) ; `angular.json` configure le remplacement de fichier pour la configuration production.
- **API_URL :** en prod, `environment.prod.ts` utilise par défaut `'/api/'` (même origine) ; à adapter si l’API est sur un autre domaine.
- **Build :** `ng build` (production par défaut) fonctionne.
- **CORS :** configuré pour localhost en dev ; en prod, ajouter les origines réelles dans `CORS_ALLOWED_ORIGINS` (ou un fichier d’environnement Django).
- **Sécurité :** en production, désactiver `DEBUG`, utiliser une `SECRET_KEY` forte et des variables d’environnement ; renforcer CORS et éventuellement ajouter une authentification sur l’API.
- **Erreurs réseau :** gérées dans les composants (ex. Contact) ; un intercepteur HTTP pourrait centraliser logs et messages.

---

## ÉTAPE 9 — Explication pédagogique

### 1. Qu’est-ce qu’une API REST ?

Une API REST expose des **ressources** (utilisateurs, projets, contacts, etc.) via des **URLs** et des **verbes HTTP** :

- **GET** : lire une ressource ou une liste (ex. `GET /api/Utilisateur/1/`).
- **POST** : créer (ex. `POST /api/PriseDeContact/` avec un JSON body).
- **PUT / PATCH** : modifier.
- **DELETE** : supprimer.

Le serveur renvoie du JSON. Dans ce projet, Django (avec DRF) joue le rôle de serveur REST.

### 2. Comment Angular consomme l’API

Angular envoie des requêtes HTTP vers ces URLs avec le service **HttpClient** (fourni par `provideHttpClient()`). Les composants n’utilisent pas HttpClient directement : des **services** (ex. UserService, ContactService) font les appels et exposent des **Observable** que les composants consomment.

### 3. Fonctionnement de HttpClient

`HttpClient.get<T>(url)` retourne un `Observable<T>`. La requête n’est envoyée que lorsqu’on **subscribe** (ou qu’on utilise l’**async** pipe). Exemple dans BaseService : `return this.http.get<T>(url);` — le type `T` permet d’avoir des données typées dans le reste de l’app.

### 4. Comment les services appellent l’API

Exemple : `UserService.getUserById(1)` appelle  
`this.baseService.get<IUser>(API_URL + 'Utilisateur/1/')`  
→ une requête GET est envoyée à `http://localhost:8000/api/Utilisateur/1/`  
→ la réponse JSON est désérialisée en objet conforme à `IUser`.

### 5. Comment les données arrivent dans les composants

Le composant appelle le service puis **subscribe** à l’Observable :

```ts
this.userService.getUserById(1).subscribe(u => this.user.set(u));
```

Ou avec l’async pipe dans le template : `user$ = this.userService.getUserById(1);` puis `{{ (user$ | async)?.nom }}`.

### 6. Comment les templates affichent les données

Les composants exposent des **signals** ou des variables (ex. `user()`) ; le template utilise la syntaxe Angular : `{{ user()?.nom }}`, `@if (messageSent()) { ... }`, etc. Les données viennent donc du flux : API → Service → Observable → subscribe / async pipe → state du composant → template.

---

## ÉTAPE 10 — Guide de lancement et déploiement

### Backend Django

1. **Environnement :**  
   `cd api-django` puis activer le venv :  
   - Windows : `venv\Scripts\activate`  
   - Linux/Mac : `source venv/bin/activate`

2. **Installation :**  
   `pip install -r requirements.txt` (si présent) ou au minimum :  
   `pip install django djangorestframework django-cors-headers`

3. **Migrations :**  
   `python manage.py migrate`

4. **Lancement :**  
   `python manage.py runserver`  
   → API disponible sur `http://localhost:8000`

5. **Tests des endpoints :**  
   - `http://localhost:8000/` → message de bienvenue  
   - `http://localhost:8000/api/Utilisateur/1/` → détail utilisateur (si id=1 existe)  
   - Créer des données via l’admin Django : `http://localhost:8000/admin/`

### Frontend Angular

1. **Installation :**  
   À la racine du projet : `npm install`

2. **Lancement :**  
   `npm start` ou `ng serve`  
   → Application sur `http://localhost:4200`

3. **Build production :**  
   `npm run build` ou `ng build`  
   → Sortie dans `dist/portfolio/` (ou configuré dans `angular.json`).

### Déploiement

- **Option A — Même serveur :** servir les fichiers statiques Angular (contenu de `dist/portfolio`) à la racine et l’API sous `/api/` (ex. avec Nginx ou avec Django en mode production). Dans `environment.prod.ts`, garder `apiUrl: '/api/'`.
- **Option B — Domaines différents :** si l’API est sur `https://api.example.com`, mettre `apiUrl: 'https://api.example.com/api/'` dans `environment.prod.ts` et ajouter `https://www.example.com` (et les origines réelles) dans `CORS_ALLOWED_ORIGINS` côté Django.
- **Sécurité :** ne pas exposer `DEBUG=True` ni une SECRET_KEY faible en production ; utiliser des variables d’environnement.

---

## ÉTAPE 11 — Rapport final

### 1. Architecture du projet

- **Monorepo** : frontend Angular (racine) + backend Django (`api-django/`).
- **API REST** : DRF, ViewSets, serializers, filtrage par `utilisateur` sur les listes.
- **Frontend** : services métier → BaseService → HttpClient ; config d’URL via environnements.

### 2. Problèmes détectés

- Modèle **PriseDeContact** : champ `Email` incorrect (référence de classe au lieu d’instance) ; champ **email** ajouté et migration créée.
- Modèle **Localisation** : `lattitde` et `Quartier` ; renommés en **latitude** et **quartier** + migration.
- **CORS** et **ALLOWED_HOSTS** non configurés ; ajout dans `settings.py`.
- **Filtrage** `?utilisateur=` non pris en charge ; implémenté dans les ViewSets concernés.
- **BaseService** : seulement get/save ; ajout de put, patch, delete.
- **Environnements Angular** : API_URL en dur ; ajout de `environment.ts` / `environment.prod.ts` et file replacement.
- **Introduction** : pas de gestion d’erreur ni d’annulation de souscription ; ajout de `takeUntilDestroyed()` et gestion d’erreur.
- **Formulaire contact** : envoyé vers `php/form.php` ; branché sur `ContactService.sendMessage()` et états succès/erreur.

### 3. Corrections appliquées

- Modèles Django et migration `0002_prisedecontact_email_localisation_fields`.
- CORS + ALLOWED_HOSTS dans `settings.py`.
- Filtrage par `utilisateur` dans les ViewSets (Projet, Experience, Service, PriseDeContact, ReseauSocial, Localisation).
- BaseService enrichi (put, patch, delete) et typage `Partial<T>` pour save.
- Fichiers d’environnement Angular et `config.ts` basé sur `environment.apiUrl`.
- Introduction : `takeUntilDestroyed()` et gestion d’erreur.
- Contact : formulaire relié à l’API, messages de succès/erreur, bouton désactivé pendant l’envoi.

### 4. Amélioration de l’API

- Endpoints et filtrage alignés avec le frontend.
- Données exposées conformes aux interfaces Angular (noms de champs : email, latitude, quartier).

### 5. Amélioration du frontend

- Configuration d’URL par environnement.
- BaseService complet et typé.
- Composant Contact entièrement branché sur l’API.
- Introduction plus robuste (souscription et erreurs).

### 6. Explication du fonctionnement

Voir **Étape 9** : flux API REST → HttpClient → BaseService → services métier → Observables → composants (subscribe / async pipe) → templates.

### 7. Guide de déploiement

Voir **Étape 10** : procédures pour lancer Django et Angular en local, build de production, et options de déploiement (même serveur vs domaines séparés, CORS et sécurité).

---

*Rapport d’audit rédigé pour vérifier et documenter la communication entre l’API Django et le frontend Angular du projet Portfolio.*
