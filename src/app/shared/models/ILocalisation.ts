/**
 * Interface pour la localisation
 * Correspond au model Django : Localisation
 */
export interface ILocalisation {
  id?: number;
  utilisateur: number; // ID de l'utilisateur
  pays: string;
  ville: string;
  latitude?: number;
  longitude?: number;
  quartier?: string;
}
