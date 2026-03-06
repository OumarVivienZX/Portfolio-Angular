import { Component, inject } from '@angular/core';
import { PortfolioStoreService } from '../../../shared/service/PortfolioStoreService';

@Component({
  selector: 'app-resume',
  imports: [],
  templateUrl: './resume.html',
  styleUrl: './resume.scss',
})
export class Resume {
  private store = inject(PortfolioStoreService);
  experiences = this.store.experiences;

  constructor() {
    this.store.load();
  }
}
