/**
 * Interface pour un service
 * Correspond au model Django : Service
 */
export interface IService {
  id?: number;
  utilisateur: number; // ID de l'utilisateur
  details: string;
  type_de_service: string;
  outils: string;
}
