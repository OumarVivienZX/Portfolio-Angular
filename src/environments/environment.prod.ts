/**
 * Configuration pour l'environnement de production
 * À adapter selon l'URL de déploiement de l'API
 */
export const environment = {
  production: true,
  apiUrl: '/api/'  // même origine en prod si Angular et Django sont servis ensemble
};
