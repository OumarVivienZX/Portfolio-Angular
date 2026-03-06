from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["GET"])
def api_home(request):
    """Page d'accueil de l'API"""
    return JsonResponse({
        "message": "Bienvenue sur l'API Portfolio",
        "version": "1.0",
        "endpoints": {
            "utilisateurs": "/api/Utilisateur/",
            "projets": "/api/Projet/",
            "experiences": "/api/Experience/",
            "services": "/api/Service/",
            "prises_de_contact": "/api/PriseDeContact/",
            "reseaux_sociaux": "/api/ReseauSocial/",
            "localisations": "/api/Localisation/",
            "admin": "/admin/"
        }
    })
