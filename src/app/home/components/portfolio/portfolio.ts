import { Component, inject } from '@angular/core';
import { PortfolioStoreService } from '../../../shared/service/PortfolioStoreService';

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
}
