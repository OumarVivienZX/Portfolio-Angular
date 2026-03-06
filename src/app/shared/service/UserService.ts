import { Injectable, inject } from "@angular/core";
import { Observable } from 'rxjs';
import { IUser } from "../models/IUser";
import { BaseService } from "../base/BaseService";
import { API_URL } from "../config";

@Injectable({ providedIn: 'root' })
export class UserService {

    private baseService = inject(BaseService);

    getUserById(id: number): Observable<IUser>{  
        return this.baseService.get<IUser>(`${API_URL}Utilisateur/${id}/`);
    }
} 