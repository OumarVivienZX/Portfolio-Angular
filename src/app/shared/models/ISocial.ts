/**
 * Interface pour un réseau social
 * Correspond au model Django : ReseauSocial
 */
export interface ISocial {
  id?: number;
  utilisateur: number; // ID de l'utilisateur
  nom_platform: string;
  lien: string; // URL
}
