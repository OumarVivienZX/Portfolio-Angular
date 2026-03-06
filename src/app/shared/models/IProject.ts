/**
 * Interface pour un projet
 * Correspond au model Django : Projet
 */
export interface IProject {
  id?: number;
  utilisateur: number; // ID de l'utilisateur
  resume: string;
  image?: string; // URL de l'image
  lien?: string; // URL du projet
}
