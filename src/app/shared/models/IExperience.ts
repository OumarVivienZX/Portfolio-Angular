/**
 * Interface pour une expérience professionnelle
 * Correspond au model Django : Experience
 */
export interface IExperience {
  id?: number;
  utilisateur: number; // ID de l'utilisateur
  date_debut: string; // Format ISO: YYYY-MM-DD
  date_fin?: string; // Format ISO: YYYY-MM-DD
  role: string;
  nom_entreprise: string;
  description?: string;
  type_de_contrat?: string;
}
