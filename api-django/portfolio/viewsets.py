from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import (
    Utilisateur, Projet, Experience, Service,
    PriseDeContact, ReseauSocial, Localisation
)
from .serializers import (
    UtilisateurSerializer, ProjetSerializer, ExperienceSerializer,
    ServiceSerializer, PriseDeContactSerializer, ReseauSocialSerializer,
    LocalisationSerializer
)
from .permissions import IsAdminUserOrReadOnly


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class PriseDeContactViewSet(viewsets.ModelViewSet):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_permissions(self):
        # allow anonymous POST to create a contact message
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class ReseauSocialViewSet(viewsets.ModelViewSet):
    queryset = ReseauSocial.objects.all()
    serializer_class = ReseauSocialSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs


class LocalisationViewSet(viewsets.ModelViewSet):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        utilisateur = self.request.query_params.get('utilisateur')
        if utilisateur is not None:
            qs = qs.filter(utilisateur_id=utilisateur)
        return qs