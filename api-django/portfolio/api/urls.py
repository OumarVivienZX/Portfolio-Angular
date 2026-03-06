from django.urls import path, include
from rest_framework.routers import DefaultRouter
from portfolio.viewsets import (
    UtilisateurViewSet, ProjetViewSet, ExperienceViewSet,
    ServiceViewSet, PriseDeContactViewSet, ReseauSocialViewSet,
    LocalisationViewSet
)

router = DefaultRouter()
router.register(r'Utilisateur', UtilisateurViewSet)
router.register(r'Projet', ProjetViewSet)
router.register(r'Experience', ExperienceViewSet)
router.register(r'Service', ServiceViewSet)
router.register(r'PriseDeContact', PriseDeContactViewSet)
router.register(r'ReseauSocial', ReseauSocialViewSet)
router.register(r'Localisation', LocalisationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
