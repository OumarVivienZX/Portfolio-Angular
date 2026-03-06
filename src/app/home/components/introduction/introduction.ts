import { Component, inject, signal } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { IUser } from '../../../shared/models';
import { UserService } from '../../../shared/service/UserService';

@Component({
  selector: 'app-introduction',
  imports: [],
  templateUrl: './introduction.html',
  styleUrl: './introduction.scss',
})
export class Introduction {
  user = signal<IUser | null>(null);
  private userService = inject(UserService);

  constructor() {
    // ID utilisateur fixe pour le portfolio
    this.userService
      .getUserById(1)
      .pipe(takeUntilDestroyed())
      .subscribe({
        next: (u) => this.user.set(u),
        error: () => this.user.set(null)
      });
  }
} 
