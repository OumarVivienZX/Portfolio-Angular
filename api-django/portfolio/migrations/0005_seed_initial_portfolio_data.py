from django.db import migrations
from django.utils import timezone


def seed_portfolio_data(apps, schema_editor):
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    Projet = apps.get_model('portfolio', 'Projet')
    Experience = apps.get_model('portfolio', 'Experience')
    Service = apps.get_model('portfolio', 'Service')
    ReseauSocial = apps.get_model('portfolio', 'ReseauSocial')
    Localisation = apps.get_model('portfolio', 'Localisation')

    try:
        user = Utilisateur.objects.get(pk=1)
    except Utilisateur.DoesNotExist:
        # Si pour une raison quelconque l'utilisateur 1 n'existe pas,
        # on ne fait rien pour éviter de créer des données orphelines.
        return

    # --- Projects (3 projects matching your previous hard-coded ones) ---
    if not Projet.objects.filter(utilisateur=user).exists():
        Projet.objects.bulk_create([
            Projet(
                utilisateur=user,
                resume='E-commerce platform',
                # L’API renverra le chemin vers le média ; ici on met un nom de fichier générique.
                image='Ecommerce.png',
                lien='',
            ),
            Projet(
                utilisateur=user,
                resume='Cafeteria management application',
                image='cantine.png',
                lien='',
            ),
            Projet(
                utilisateur=user,
                resume='Carpooling application',
                image='carpooling.png',
                lien='',
            ),
        ])

    # --- Experiences (from the Resume section content) ---
    if not Experience.objects.filter(utilisateur=user).exists():
        Experience.objects.bulk_create([
            Experience(
                utilisateur=user,
                date_debut=timezone.datetime(2023, 1, 1).date(),
                date_fin=timezone.datetime(2025, 12, 31).date(),
                role='Bachelor’s Degree in Software Engineering',
                nom_entreprise='Institut Ivoirien de Technologie',
                description=(
                    "Software Engineering program at the Ivorian Institute of Technology. "
                    "Currently in the third year of the Bachelor’s degree, with a strong "
                    "focus on web development, databases, and software architecture."
                ),
                type_de_contrat='Education',
            ),
            Experience(
                utilisateur=user,
                date_debut=timezone.datetime(2023, 6, 1).date(),
                date_fin=None,
                role='Python Certification (In Progress)',
                nom_entreprise='Professional training',
                description=(
                    "Ongoing professional Python certification focused on backend "
                    "development, object-oriented programming, the Django framework, "
                    "and REST API development."
                ),
                type_de_contrat='Certification',
            ),
        ])

    # --- Services (generic but meaningful services for the Services section) ---
    if not Service.objects.filter(utilisateur=user).exists():
        Service.objects.bulk_create([
            Service(
                utilisateur=user,
                type_de_service='Frontend Development',
                details="Design and development of modern user interfaces with Angular, HTML5, CSS3 and JavaScript.",
                outils='Angular, HTML5, CSS3, TypeScript, JavaScript',
            ),
            Service(
                utilisateur=user,
                type_de_service='Backend Development',
                details="Creation of secure and high-performance REST APIs with Python and Django.",
                outils='Python, Django, Django REST Framework',
            ),
            Service(
                utilisateur=user,
                type_de_service='Integration & Deployment',
                details="Integration between frontend and backend, deployment to cloud platforms and basic CI/CD.",
                outils='Git, GitHub, CI/CD, Docker (basic)',
            ),
        ])

    # --- Réseaux sociaux (GitHub, LinkedIn, Facebook) ---
    if not ReseauSocial.objects.filter(utilisateur=user).exists():
        ReseauSocial.objects.bulk_create([
            ReseauSocial(
                utilisateur=user,
                nom_platform='GitHub',
                lien='https://github.com/OumarVivienZX/',
            ),
            ReseauSocial(
                utilisateur=user,
                nom_platform='LinkedIn',
                lien='https://www.linkedin.com/in/oumar-vivien-konan-426109319',
            ),
            ReseauSocial(
                utilisateur=user,
                nom_platform='Facebook',
                lien='https://www.facebook.com/profile.php?id=100095585340548',
            ),
        ])

    # --- Location (simple default entry, can be edited later in admin) ---
    if not Localisation.objects.filter(utilisateur=user).exists():
        Localisation.objects.create(
            utilisateur=user,
            pays="Côte d'Ivoire",
            ville='Abidjan',
            quartier='',
            latitude=None,
            longitude=None,
        )


def unseed_portfolio_data(apps, schema_editor):
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    Projet = apps.get_model('portfolio', 'Projet')
    Experience = apps.get_model('portfolio', 'Experience')
    Service = apps.get_model('portfolio', 'Service')
    ReseauSocial = apps.get_model('portfolio', 'ReseauSocial')
    Localisation = apps.get_model('portfolio', 'Localisation')

    try:
        user = Utilisateur.objects.get(pk=1)
    except Utilisateur.DoesNotExist:
        return

    Projet.objects.filter(utilisateur=user).delete()
    Experience.objects.filter(utilisateur=user).delete()
    Service.objects.filter(utilisateur=user).delete()
    ReseauSocial.objects.filter(utilisateur=user).delete()
    Localisation.objects.filter(utilisateur=user).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_create_default_user'),
    ]

    operations = [
        migrations.RunPython(seed_portfolio_data, unseed_portfolio_data),
    ]

from datetime import date

from django.db import migrations


def seed_portfolio_data(apps, schema_editor):
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    Projet = apps.get_model('portfolio', 'Projet')
    Experience = apps.get_model('portfolio', 'Experience')
    Service = apps.get_model('portfolio', 'Service')
    ReseauSocial = apps.get_model('portfolio', 'ReseauSocial')
    Localisation = apps.get_model('portfolio', 'Localisation')

    try:
        user = Utilisateur.objects.get(pk=1)
    except Utilisateur.DoesNotExist:
        return

    # Projets
    if not Projet.objects.filter(utilisateur=user).exists():
        Projet.objects.bulk_create(
            [
                Projet(
                    utilisateur=user,
                    resume="E‑commerce web app (Angular + Django)",
                    lien="https://github.com/OumarVivienZX",
                ),
                Projet(
                    utilisateur=user,
                    resume="Portfolio personnel (Angular + Django REST)",
                    lien="https://portfolio-konan.netlify.app",
                ),
                Projet(
                    utilisateur=user,
                    resume="Application mobile Flutter (gestion de tâches)",
                    lien="",
                ),
            ]
        )

    # Expériences
    if not Experience.objects.filter(utilisateur=user).exists():
        Experience.objects.bulk_create(
            [
                Experience(
                    utilisateur=user,
                    date_debut=date(2023, 1, 1),
                    date_fin=None,
                    role="Full‑stack Developer (Django & Flutter)",
                    nom_entreprise="Freelance",
                    description=(
                        "Développement d'applications web avec Django REST API "
                        "et d'applications mobiles Flutter pour des clients."
                    ),
                    type_de_contrat="Freelance",
                ),
            ]
        )

    # Services
    if not Service.objects.filter(utilisateur=user).exists():
        Service.objects.bulk_create(
            [
                Service(
                    utilisateur=user,
                    type_de_service="Backend Development",
                    details="APIs REST sécurisées avec Django & Django REST Framework.",
                    outils="Django, DRF, PostgreSQL",
                ),
                Service(
                    utilisateur=user,
                    type_de_service="Mobile Applications",
                    details="Applications mobiles Flutter connectées à des APIs.",
                    outils="Flutter, Dart, Firebase",
                ),
                Service(
                    utilisateur=user,
                    type_de_service="Frontend Web",
                    details="Interfaces modernes et responsives en Angular.",
                    outils="Angular, HTML, SCSS",
                ),
            ]
        )

    # Réseaux sociaux
    if not ReseauSocial.objects.filter(utilisateur=user).exists():
        ReseauSocial.objects.bulk_create(
            [
                ReseauSocial(
                    utilisateur=user,
                    nom_platform="Facebook",
                    lien="https://www.facebook.com/profile.php?id=100095585340548",
                ),
                ReseauSocial(
                    utilisateur=user,
                    nom_platform="LinkedIn",
                    lien="https://www.linkedin.com/in/oumar-vivien-konan-426109319",
                ),
                ReseauSocial(
                    utilisateur=user,
                    nom_platform="GitHub",
                    lien="https://github.com/OumarVivienZX",
                ),
            ]
        )

    # Localisation
    if not Localisation.objects.filter(utilisateur=user).exists():
        Localisation.objects.create(
            utilisateur=user,
            pays="Côte d'Ivoire",
            ville="Grand-Bassam",
            quartier="",
        )


def unseed_portfolio_data(apps, schema_editor):
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    Projet = apps.get_model('portfolio', 'Projet')
    Experience = apps.get_model('portfolio', 'Experience')
    Service = apps.get_model('portfolio', 'Service')
    ReseauSocial = apps.get_model('portfolio', 'ReseauSocial')
    Localisation = apps.get_model('portfolio', 'Localisation')

    try:
        user = Utilisateur.objects.get(pk=1)
    except Utilisateur.DoesNotExist:
        return

    Projet.objects.filter(utilisateur=user).delete()
    Experience.objects.filter(utilisateur=user).delete()
    Service.objects.filter(utilisateur=user).delete()
    ReseauSocial.objects.filter(utilisateur=user).delete()
    Localisation.objects.filter(utilisateur=user).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_create_default_user'),
    ]

    operations = [
        migrations.RunPython(seed_portfolio_data, unseed_portfolio_data),
    ]

