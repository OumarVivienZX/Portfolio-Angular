import { Component, inject } from '@angular/core';
import { OfferService } from '../../../shared/service/OfferService';
@Component({
  selector: 'app-services',
  imports: [],
  templateUrl: './services.html',
  styleUrl: './services.scss',
})
export class Services {
  private offerService = inject(OfferService);

}
