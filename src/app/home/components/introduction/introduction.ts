import { Component, inject } from '@angular/core';
import { PortfolioStoreService } from '../../../shared/service/PortfolioStoreService';

@Component({
  selector: 'app-introduction',
  imports: [],
  templateUrl: './introduction.html',
  styleUrl: './introduction.scss',
})
export class Introduction {
  private store = inject(PortfolioStoreService);
  user = this.store.user;

  constructor() {
    this.store.load();
  }
} 
