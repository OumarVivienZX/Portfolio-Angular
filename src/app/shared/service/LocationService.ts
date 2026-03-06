import { Injectable, inject } from "@angular/core";
import { Observable } from 'rxjs';
import { ILocalisation } from "../models/ILocalisation";
import { BaseService } from "../base/BaseService";
import { API_URL } from "../config";

@Injectable({ providedIn: 'root' })
export class LocationService {

    private baseService = inject(BaseService);

    getAllLocationByUserId(id: number): Observable<ILocalisation[]>{  
        return this.baseService.get<ILocalisation[]>(`${API_URL}Localisation/?utilisateur=${id}`);
    }
}