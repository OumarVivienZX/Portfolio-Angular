from django.db import migrations
from django.utils import timezone


def update_portfolio_data(apps, schema_editor):
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    Projet = apps.get_model('portfolio', 'Projet')
    Experience = apps.get_model('portfolio', 'Experience')

    try:
        user = Utilisateur.objects.get(pk=1)
    except Utilisateur.DoesNotExist:
        return

    # --- Ensure projects use correct asset image paths and exist ---
    projects_spec = [
        {
            "resume": "E-commerce platform",
            "image": "assets/images/Ecommerce.png",
        },
        {
            "resume": "Cafeteria management application",
            "image": "assets/images/cantine.png",
        },
        {
            "resume": "Carpooling application",
            "image": "assets/images/carpooling.png",
        },
    ]

    for spec in projects_spec:
        proj, created = Projet.objects.get_or_create(
            utilisateur=user,
            resume=spec["resume"],
            defaults={
                "image": spec["image"],
                "lien": "",
            },
        )
        if not created:
            proj.image = spec["image"]
            if proj.lien is None:
                proj.lien = ""
            proj.save()

    # --- Ensure the two education/Certification experiences are in English ---
    # Education
    exp_edu, _ = Experience.objects.get_or_create(
        utilisateur=user,
        role="Bachelor’s Degree in Software Engineering",
        nom_entreprise="Ivorian Institute of Technology",
        defaults={
            "date_debut": timezone.datetime(2023, 1, 1).date(),
            "date_fin": timezone.datetime(2025, 12, 31).date(),
            "description": (
                "Software Engineering program at the Ivorian Institute of Technology. "
                "Currently in the third year of the Bachelor’s degree, with a strong "
                "focus on web development, databases, and software architecture."
            ),
            "type_de_contrat": "Education",
        },
    )
    if exp_edu:
        exp_edu.description = (
            "Software Engineering program at the Ivorian Institute of Technology. "
            "Currently in the third year of the Bachelor’s degree, with a strong "
            "focus on web development, databases, and software architecture."
        )
        exp_edu.type_de_contrat = "Education"
        exp_edu.save()

    # Certification
    exp_cert, _ = Experience.objects.get_or_create(
        utilisateur=user,
        role="Python Certification (In Progress)",
        nom_entreprise="Professional training",
        defaults={
            "date_debut": timezone.datetime(2023, 6, 1).date(),
            "date_fin": None,
            "description": (
                "Ongoing professional Python certification focused on backend "
                "development, object-oriented programming, the Django framework, "
                "and REST API development."
            ),
            "type_de_contrat": "Certification",
        },
    )
    if exp_cert:
        exp_cert.description = (
            "Ongoing professional Python certification focused on backend "
            "development, object-oriented programming, the Django framework, "
            "and REST API development."
        )
        exp_cert.type_de_contrat = "Certification"
        exp_cert.save()

    # --- Add professional experience at IFLYSIM (web developer & graphic design) ---
    if not Experience.objects.filter(
        utilisateur=user,
        role__icontains="Web Developer",
        nom_entreprise__icontains="IFLYSIM",
    ).exists():
        Experience.objects.create(
            utilisateur=user,
            date_debut=timezone.datetime(2024, 1, 1).date(),
            date_fin=None,
            role="Web Developer & Graphic Designer",
            nom_entreprise="IFLYSIM",
            description=(
                "Worked as a web developer at IFLYSIM, creating and maintaining web "
                "pages and producing marketing visuals and posters (graphic design)."
            ),
            type_de_contrat="Web development",
        )


def reverse_update_portfolio_data(apps, schema_editor):
    Utilisateur = apps.get_model('portfolio', 'Utilisateur')
    Projet = apps.get_model('portfolio', 'Projet')
    Experience = apps.get_model('portfolio', 'Experience')

    try:
        user = Utilisateur.objects.get(pk=1)
    except Utilisateur.DoesNotExist:
        return

    # Remove IFLYSIM experience if present
    Experience.objects.filter(
        utilisateur=user,
        nom_entreprise__icontains="IFLYSIM",
    ).delete()

    # We don't aggressively delete/update the other records in reverse to avoid
    # losing manual edits done in the admin.


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0005_seed_initial_portfolio_data"),
    ]

    operations = [
        migrations.RunPython(update_portfolio_data, reverse_update_portfolio_data),
    ]

