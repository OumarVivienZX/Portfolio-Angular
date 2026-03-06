from django.db import migrations
from django.utils import timezone


def sync_portfolio_with_admin_choices(apps, schema_editor):
    """
    Aligne les données de la base avec les valeurs que tu as décrites
    pour l'utilisateur 1 (experiences, projects, services).
    """
    Utilisateur = apps.get_model("portfolio", "Utilisateur")
    Experience = apps.get_model("portfolio", "Experience")
    Projet = apps.get_model("portfolio", "Projet")
    Service = apps.get_model("portfolio", "Service")

    try:
        user = Utilisateur.objects.get(pk=1)
    except Utilisateur.DoesNotExist:
        return

    # --- EXPERIENCES ---
    # 1) Bachelor’s Degree in Software Engineering – Ivorian Institute of Technology
    exp_bachelor, _ = Experience.objects.get_or_create(
        utilisateur=user,
        role="Bachelor’s Degree in Software Engineering",
        nom_entreprise="Ivorian Institute of Technology",
        defaults={
            "date_debut": timezone.datetime(2023, 1, 1).date(),
            "date_fin": timezone.datetime(2026, 7, 15).date(),
            "type_de_contrat": "Education",
            "description": (
                "Bachelor’s degree in Software Engineering at the Ivorian Institute of Technology, "
                "with a strong focus on web development, databases and software architecture."
            ),
        },
    )
    exp_bachelor.date_debut = timezone.datetime(2023, 1, 1).date()
    exp_bachelor.date_fin = timezone.datetime(2026, 7, 15).date()
    exp_bachelor.type_de_contrat = "Education"
    exp_bachelor.save()

    # 2) Python Certification (In Progress) – Professional training
    exp_python, _ = Experience.objects.get_or_create(
        utilisateur=user,
        role="Python Certification (In Progress)",
        nom_entreprise="Professional training",
        defaults={
            "date_debut": timezone.datetime(2023, 6, 1).date(),
            "date_fin": None,
            "type_de_contrat": "Certification",
            "description": (
                "Ongoing professional Python certification focused on backend development, "
                "object-oriented programming, the Django framework and REST API development."
            ),
        },
    )
    exp_python.date_debut = timezone.datetime(2023, 6, 1).date()
    exp_python.date_fin = None
    exp_python.type_de_contrat = "Certification"
    exp_python.save()

    # 3) Web Developer & Graphic Designer – IFLYSIM
    exp_iflysim, _ = Experience.objects.get_or_create(
        utilisateur=user,
        role="Web Developer & Graphic Designer",
        nom_entreprise="IFLYSIM",
        defaults={
            "date_debut": timezone.datetime(2025, 6, 15).date(),
            "date_fin": None,
            "type_de_contrat": "Web development",
            "description": (
                "Worked as a web developer at IFLYSIM, building web pages and creating "
                "marketing posters and visuals (graphic design)."
            ),
        },
    )
    exp_iflysim.date_debut = timezone.datetime(2025, 6, 15).date()
    exp_iflysim.date_fin = None
    exp_iflysim.type_de_contrat = "Web development"
    exp_iflysim.save()

    # --- PROJECTS ---
    # On force les chemins d'images pour correspondre aux assets Angular
    proj_ecom, _ = Projet.objects.get_or_create(
        utilisateur=user,
        resume="E-commerce platform for Otaku's",
        defaults={
            "image": "assets/images/Ecommerce.png",
            "lien": "",
        },
    )
    proj_ecom.image = "assets/images/Ecommerce.png"
    proj_ecom.save()

    proj_cantine, _ = Projet.objects.get_or_create(
        utilisateur=user,
        resume="Cafeteria management application",
        defaults={
            "image": "assets/images/cantine.png",
            "lien": "",
        },
    )
    proj_cantine.image = "assets/images/cantine.png"
    proj_cantine.save()

    proj_carpooling, _ = Projet.objects.get_or_create(
        utilisateur=user,
        resume="Carpooling application",
        defaults={
            "image": "assets/images/carpooling.png",
            "lien": "",
        },
    )
    proj_carpooling.image = "assets/images/carpooling.png"
    proj_carpooling.save()

    # Optionnel : on peut supprimer les autres projets associés à l'utilisateur
    Projet.objects.filter(utilisateur=user).exclude(
        id__in=[proj_ecom.id, proj_cantine.id, proj_carpooling.id]
    ).delete()

    # --- SERVICES ---
    srv_backend, _ = Service.objects.get_or_create(
        utilisateur=user,
        type_de_service="Backend Development",
        defaults={
            "details": "Secure REST APIs with Django & Django REST Framework.",
            "outils": "Django, DRF, PostgreSQL",
        },
    )
    srv_backend.details = "Secure REST APIs with Django & Django REST Framework."
    srv_backend.outils = "Django, DRF, PostgreSQL"
    srv_backend.save()

    srv_mobile, _ = Service.objects.get_or_create(
        utilisateur=user,
        type_de_service="Mobile Applications",
        defaults={
            "details": "Flutter mobile applications connected to APIs.",
            "outils": "Flutter, Dart, Firebase",
        },
    )
    srv_mobile.details = "Flutter mobile applications connected to APIs."
    srv_mobile.outils = "Flutter, Dart, Firebase"
    srv_mobile.save()

    srv_frontend, _ = Service.objects.get_or_create(
        utilisateur=user,
        type_de_service="Frontend Web",
        defaults={
            "details": "Modern and responsive interfaces in Angular.",
            "outils": "Angular, HTML, SCSS",
        },
    )
    srv_frontend.details = "Modern and responsive interfaces in Angular."
    srv_frontend.outils = "Angular, HTML, SCSS"
    srv_frontend.save()


def reverse_sync_portfolio_with_admin_choices(apps, schema_editor):
    # On ne supprime rien en reverse pour éviter de perdre des données saisies à la main.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0006_update_portfolio_seed"),
    ]

    operations = [
        migrations.RunPython(
            sync_portfolio_with_admin_choices,
            reverse_sync_portfolio_with_admin_choices,
        ),
    ]

