from django.db import migrations


def create_default_user(apps, schema_editor):
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    if Utilisateur.objects.exists():
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
        ('portfolio', '0003_fix_utilisateur_donnees'),
    ]

    operations = [
        migrations.RunPython(create_default_user, delete_default_user),
    ]
