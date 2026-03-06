import { Component, inject } from '@angular/core';
import { PortfolioStoreService } from '../../../shared/service/PortfolioStoreService';
@Component({
  selector: 'app-services',
  imports: [],
  templateUrl: './services.html',
  styleUrl: './services.scss',
})
export class Services {
  private store = inject(PortfolioStoreService);
  services = this.store.services;

  constructor() {
    this.store.load();
  }
}
