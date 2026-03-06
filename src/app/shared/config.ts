import { environment } from '../../environments/environment';

/**
 * URL de base de l'API Django.
 * En dev : http://localhost:8000/api/
 * En prod : définie dans environment.prod.ts (ex: /api/ si même serveur)
 */
export const API_URL = environment.apiUrl;
