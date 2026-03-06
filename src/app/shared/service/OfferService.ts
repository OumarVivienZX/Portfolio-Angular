import { Injectable, inject } from "@angular/core";
import { Observable } from 'rxjs';
import { IService } from "../models/IService";
import { BaseService } from "../base/BaseService";
import { API_URL } from "../config";

@Injectable({ providedIn: 'root' })
export class OfferService {

    private baseService = inject(BaseService);
    
    getAllServiceByUserId(id: number): Observable<IService[]>{  
        return this.baseService.get<IService[]>(`${API_URL}Service/?utilisateur=${id}`);
    }
} 