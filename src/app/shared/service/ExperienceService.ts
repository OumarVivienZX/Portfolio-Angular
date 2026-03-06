import { Injectable, inject } from "@angular/core";
import { Observable } from 'rxjs';
import  { IExperience } from "../models/IExperience";
import { BaseService } from "../base/BaseService";
import { API_URL } from "../config";

@Injectable({ providedIn: 'root' })
export class ExperienceService {

    private baseService = inject(BaseService);
    
    getAllExperienceByUserId(id: number): Observable<IExperience[]>{  
        return this.baseService.get<IExperience[]>(`${API_URL}Experience/?utilisateur=${id}`);
    }  
}
