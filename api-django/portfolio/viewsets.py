from rest_framework import viewsets
from .models import (
    Utilisateur, Projet, Experience, Service,
    PriseDeContact, ReseauSocial, Localisation
)
from .serializers import (
    UtilisateurSerializer, ProjetSerializer, ExperienceSerializer,
    ServiceSerializer, PriseDeContactSerializer, ReseauSocialSerializer,
    LocalisationSerializer
)


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class PriseDeContactViewSet(viewsets.ModelViewSet):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class ReseauSocialViewSet(viewsets.ModelViewSet):
    queryset = ReseauSocial.objects.all()
    serializer_class = ReseauSocialSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class LocalisationViewSet(viewsets.ModelViewSet):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs