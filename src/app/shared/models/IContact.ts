export interface IContact {
  id?: number;
  utilisateur: number; // ID de l'utilisateur
  nom: string;
  objet: string;
  message: string;
  email: string;
  date_envoi?: string; // Format ISO: YYYY-MM-DDTHH:mm:ssZ
}