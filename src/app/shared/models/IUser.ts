/**
 * Interface pour l'utilisateur
 * Correspond au model Django : Utilisateur
 */
export interface IUser {
  id?: number;
  nom: string;
  prenom: string;
  photo_profil?: string; // URL de l'image
  description?: string;
  age?: number;
  email: string;
  lien?: string; // URL
  cv?: string; // URL du fichier
  telephone?: string;
}
