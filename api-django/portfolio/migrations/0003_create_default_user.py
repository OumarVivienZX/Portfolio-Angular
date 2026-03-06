from django.db import migrations


def create_default_user(apps, schema_editor):
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    if Utilisateur.objects.exists():
        # Ne rien faire si un utilisateur existe déjà en base
        return

    Utilisateur.objects.create(
        nom='KONAN',
        prenom='OUMAR VIVIEN',
        description='Fullstack web developer',
        age=21,
        email='oumarvivienkonan9@gmail.com',
        lien='https://portfolio-konan.netlify.app',
        telephone='0757477890',
    )


def delete_default_user(apps, schema_editor):
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    Utilisateur.objects.filter(email='oumarvivienkonan9@gmail.com').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_prisedecontact_email_localisation_fields'),
    ]

    operations = [
        migrations.RunPython(create_default_user, delete_default_user),
    ]

