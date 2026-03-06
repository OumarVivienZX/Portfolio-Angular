# Portfolio

This project was generated using [Angular CLI](https://github.com/angular/angular-cli) version 21.0.3.

## Development server

To start a local development server, run:

```bash
ng serve
```

Once the server is running, open your browser and navigate to `http://localhost:4200/`. The application will automatically reload whenever you modify any of the source files.

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

Le frontend interagit avec une API Django située dans le dossier `api-django`.
La constante `API_URL` se trouve dans `src/app/shared/config.ts` et pointe par défaut vers :

```ts
export const API_URL = 'http://localhost:8000/api/';
```

Les services du dossier `src/app/shared/service` offrent des méthodes retournant des
`Observable` typés pour récupérer les données du backend (utilisateur, projets,
expériences, etc.) et envoyer des formulaires de contact.

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

### Frontend

1. Démarrer l'application Angular :
   ```bash
   npm install
   npm run start
   ```
2. Le composant `Introduction` montre un exemple d'appel à `UserService.getUserById(1)`
et met à jour l'interface via une `signal`.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
