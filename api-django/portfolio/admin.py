from django.contrib import admin
from .models import (
    Utilisateur, Projet, Experience, Service,
    PriseDeContact, ReseauSocial, Localisation
)


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'email', 'description')
    list_filter = ('nom',)
    search_fields = ('nom', 'prenom', 'email')
    ordering = ('id',)
    list_editable = ('nom', 'prenom', 'email', 'description')


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'resume', 'image', 'lien')
    list_filter = ('utilisateur',)
    search_fields = ('resume',)
    list_editable = ('resume', 'image', 'lien')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'role', 'nom_entreprise', 'date_debut', 'date_fin', 'type_de_contrat')
    list_filter = ('utilisateur',)
    search_fields = ('role', 'nom_entreprise')
    list_editable = ('role', 'nom_entreprise', 'date_debut', 'date_fin', 'type_de_contrat')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'type_de_service', 'details', 'outils')
    list_filter = ('utilisateur',)
    list_editable = ('type_de_service', 'details', 'outils')


@admin.register(PriseDeContact)
class PriseDeContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'nom', 'email', 'objet')
    list_filter = ('utilisateur',)
    search_fields = ('nom', 'email', 'objet')


@admin.register(ReseauSocial)
class ReseauSocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'nom_platform', 'lien')
    list_filter = ('utilisateur',)
    list_editable = ('nom_platform', 'lien')


@admin.register(Localisation)
class LocalisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'ville', 'pays', 'quartier')
    list_filter = ('utilisateur',)
    list_editable = ('ville', 'pays', 'quartier')
