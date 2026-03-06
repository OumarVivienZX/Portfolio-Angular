import { Component, inject } from '@angular/core';
import { PortfolioStoreService } from '../../../shared/service/PortfolioStoreService';
import { IProject } from '../../../shared/models';

@Component({
  selector: 'app-portfolio',
  imports: [],
  templateUrl: './portfolio.html',
  styleUrl: './portfolio.scss',
})
export class Portfolio {
  private store = inject(PortfolioStoreService);
  projects = this.store.projects;

  constructor() {
    this.store.load();
  }

  getProjectImage(p: IProject): string {
    const title = (p.resume || '').toLowerCase();

    if (title.includes('cafeteria')) {
      return 'assets/images/cantine.png';
    }

    if (title.includes('carpooling')) {
      return 'assets/images/carpooling.png';
    }

    // Par défaut : projet e-commerce
    return 'assets/images/Ecommerce.png';
  }
}
