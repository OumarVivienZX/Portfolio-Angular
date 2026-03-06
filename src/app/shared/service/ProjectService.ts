import { Injectable, inject } from "@angular/core";
import { Observable } from 'rxjs';
import { IProject } from "../models/IProject";
import { BaseService } from "../base/BaseService";
import { API_URL } from "../config";

@Injectable({ providedIn: 'root' })
export class ProjectService {

    private baseService = inject(BaseService);
    
    getAllProjectByUserId(id: number): Observable<IProject[]>{  
        return this.baseService.get<IProject[]>(`${API_URL}Projet/?utilisateur=${id}`);
    }
} 