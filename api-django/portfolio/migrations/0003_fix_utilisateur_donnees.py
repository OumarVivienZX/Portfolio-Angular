# Migration pour corriger les données de l'utilisateur (nom, prénom, description)

from django.db import migrations


def fix_utilisateur_donnees(apps, schema_editor):
    """Corrige les données de l'utilisateur id=1 : KONAN OUMAR VIVIEN, fullstack web developer"""
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    try:
        u = Utilisateur.objects.get(pk=1)
        u.nom = 'KONAN'
        u.prenom = 'OUMAR VIVIEN'
        u.description = 'fullstack web developer'
        u.save()
    except Utilisateur.DoesNotExist:
        pass  # L'utilisateur n'existe pas encore, on ignore


def reverse_fix(apps, schema_editor):
    pass  # Pas de rollback pour une correction de données


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_prisedecontact_email_localisation_fields'),
    ]

    operations = [
        migrations.RunPython(fix_utilisateur_donnees, reverse_fix),
    ]
