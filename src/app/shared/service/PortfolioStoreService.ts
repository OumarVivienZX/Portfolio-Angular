import { Injectable, inject, signal } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { IUser, IProject, IExperience, IService, ISocial, ILocalisation } from '../models';
import { UserService } from './UserService';
import { ProjectService } from './ProjectService';
import { ExperienceService } from './ExperienceService';
import { OfferService } from './OfferService';
import { SocialService } from './SocialService';
import { LocationService } from './LocationService';

@Injectable({ providedIn: 'root' })
export class PortfolioStoreService {
  private readonly userId = 1;

  private userService = inject(UserService);
  private projectService = inject(ProjectService);
  private experienceService = inject(ExperienceService);
  private offerService = inject(OfferService);
  private socialService = inject(SocialService);
  private locationService = inject(LocationService);

  user = signal<IUser | null>(null);
  projects = signal<IProject[]>([]);
  experiences = signal<IExperience[]>([]);
  services = signal<IService[]>([]);
  socials = signal<ISocial[]>([]);
  locations = signal<ILocalisation[]>([]);

  loaded = signal(false);
  loading = signal(false);
  error = signal<string | null>(null);

  load(): void {
    if (this.loading() || this.loaded()) return;
    this.loading.set(true);
    this.error.set(null);

    // Profil
    this.userService
      .getUserById(this.userId)
      .pipe(takeUntilDestroyed())
      .subscribe({
        next: (u) => this.user.set(u),
        error: () => this.user.set(null),
      });

    // Collections
    this.projectService
      .getAllProjectByUserId(this.userId)
      .pipe(takeUntilDestroyed())
      .subscribe({
        next: (p) => this.projects.set(p ?? []),
        error: () => this.projects.set([]),
      });

    this.experienceService
      .getAllExperienceByUserId(this.userId)
      .pipe(takeUntilDestroyed())
      .subscribe({
        next: (e) => this.experiences.set(e ?? []),
        error: () => this.experiences.set([]),
      });

    this.offerService
      .getAllServiceByUserId(this.userId)
      .pipe(takeUntilDestroyed())
      .subscribe({
        next: (s) => this.services.set(s ?? []),
        error: () => this.services.set([]),
      });

    this.socialService
      .getAllSocialByUserId(this.userId)
      .pipe(takeUntilDestroyed())
      .subscribe({
        next: (s) => this.socials.set(s ?? []),
        error: () => this.socials.set([]),
      });

    this.locationService
      .getAllLocationByUserId(this.userId)
      .pipe(takeUntilDestroyed())
      .subscribe({
        next: (l) => this.locations.set(l ?? []),
        error: () => this.locations.set([]),
      });

    // On considère "loaded" quand les appels sont lancés (simple et suffisant pour l'UI)
    this.loading.set(false);
    this.loaded.set(true);
  }
}

