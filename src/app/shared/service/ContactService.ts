import { Injectable, inject } from "@angular/core";
import { Observable } from 'rxjs';
import { IContact } from "../models/IContact";
import { BaseService } from "../base/BaseService";
import { API_URL } from "../config";

@Injectable({ providedIn: 'root' })
export class ContactService {

    private baseService = inject(BaseService);
    
    getAllContactByUserId(id: number): Observable<IContact[]>{  
        return this.baseService.get<IContact[]>(`${API_URL}PriseDeContact/?utilisateur=${id}`);
    }

    /**
     * envoi d'un nouveau message de contact
     */
    sendMessage(data: IContact): Observable<IContact>{
        return this.baseService.save<IContact>(`${API_URL}PriseDeContact/`, data);
    }
} 