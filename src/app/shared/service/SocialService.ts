import { Injectable, inject } from "@angular/core";
import { Observable } from 'rxjs';
import { ISocial } from "../models/ISocial";
import { BaseService } from "../base/BaseService";
import { API_URL } from "../config";

@Injectable({ providedIn: 'root' })
export class SocialService {

    private baseService = inject(BaseService);

    getAllSocialByUserId(id: number): Observable<ISocial[]>{  
        return this.baseService.get<ISocial[]>(`${API_URL}ReseauSocial/?utilisateur=${id}`);
    }
} 