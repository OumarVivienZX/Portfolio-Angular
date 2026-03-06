import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

/**
 * Service de base pour les appels HTTP à l'API REST.
 * Centralise les méthodes GET, POST, PUT, PATCH, DELETE avec typage générique.
 */
@Injectable({
  providedIn: 'root'
})
export class BaseService {
  constructor(private http: HttpClient) {}

  /** GET : récupérer une ressource ou une liste */
  get<T>(url: string): Observable<T> {
    return this.http.get<T>(url);
  }

  /** POST : créer une nouvelle ressource */
  save<T>(url: string, data: Partial<T>): Observable<T> {
    return this.http.post<T>(url, data);
  }

  /** PUT : mise à jour complète d'une ressource */
  put<T>(url: string, data: T): Observable<T> {
    return this.http.put<T>(url, data);
  }

  /** PATCH : mise à jour partielle d'une ressource */
  patch<T>(url: string, data: Partial<T>): Observable<T> {
    return this.http.patch<T>(url, data);
  }

  /** DELETE : supprimer une ressource */
  delete<T>(url: string): Observable<T> {
    return this.http.delete<T>(url);
  }
}
