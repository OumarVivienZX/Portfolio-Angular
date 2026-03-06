"""
Signal pour envoyer un email à koumarvivien@gmail.com lors d'un nouveau message de contact.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import PriseDeContact

EMAIL_DESTINATAIRE = 'koumarvivien@gmail.com'


@receiver(post_save, sender=PriseDeContact)
def envoyer_email_contact(sender, instance, created, **kwargs):
    """Envoie un email au propriétaire du portfolio quand un message est reçu."""
    if not created:
        return

    sujet = f"[Portfolio] Nouveau message : {instance.objet}"
    message = f"""
Nouveau message reçu depuis votre portfolio :

De : {instance.nom}
Email : {instance.email}
Objet : {instance.objet}

Message :
{instance.message}
"""
    try:
        send_mail(
            subject=sujet,
            message=message.strip(),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[EMAIL_DESTINATAIRE],
            fail_silently=False,
        )
    except Exception:
        # Ne pas bloquer la sauvegarde si l'email échoue
        pass
