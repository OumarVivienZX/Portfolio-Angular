/**
 * Configuration pour l'environnement de production
 * À adapter selon l'URL de déploiement de l'API
 */
export const environment = {
  production: true,
  /**
   * En déploiement séparé (Netlify pour Angular + backend ailleurs),
   * renseigner ici l'URL publique du backend Django.
   * Exemple: https://portfolio-api.onrender.com/api/
   */
  apiUrl: 'https://CHANGE_ME_BACKEND_DOMAIN/api/'
};
