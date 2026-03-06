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
            "utilisateurs": "/api/utilisateurs/",
            "projets": "/api/projets/",
            "experiences": "/api/experiences/",
            "services": "/api/services/",
            "prises_de_contact": "/api/prises-de-contact/",
            "reseaux_sociaux": "/api/reseaux-sociaux/",
            "localisations": "/api/localisations/",
            "admin": "/admin/"
        }
    })
