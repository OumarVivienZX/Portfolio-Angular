import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ContactService } from '../../../shared/service/ContactService';
import { IContact } from '../../../shared/models';

@Component({
  selector: 'app-contact',
  imports: [FormsModule],
  templateUrl: './contact.html',
  styleUrl: './contact.scss',
})
export class Contact {
  private contactService = inject(ContactService);

  /** ID utilisateur du portfolio (à adapter si multi-utilisateurs) */
  private readonly userId = 1;

  sending = signal(false);
  messageSent = signal(false);
  error = signal<string | null>(null);

  nom = '';
  email = '';
  objet = '';
  message = '';

  onSubmit(): void {
    this.error.set(null);
    this.messageSent.set(false);
    this.sending.set(true);

    const data: IContact = {
      utilisateur: this.userId,
      nom: this.nom,
      email: this.email,
      objet: this.objet,
      message: this.message
    };

    this.contactService.sendMessage(data).subscribe({
      next: () => {
        this.sending.set(false);
        this.messageSent.set(true);
        this.nom = '';
        this.email = '';
        this.objet = '';
        this.message = '';
      },
      error: (err) => {
        this.sending.set(false);
        this.error.set(err?.message || 'Erreur lors de l\'envoi du message.');
      }
    });
  }
}
