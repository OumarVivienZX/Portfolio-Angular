from django.db import models
from django.core.validators import URLValidator,EmailValidator


# Create your models here.
class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    photo_profil = models.ImageField(upload_to='profiles/', null=True, blank=True)
    description = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    lien = models.URLField(blank=True)
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Projet (models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='projets')
    resume = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    lien = models.URLField(blank=True)

    def __str__(self):
        return self.resume


class Experience(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='experiences')
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=100)
    nom_entreprise = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type_de_contrat = models.CharField(max_length=50, blank=True)

    def __str__(self):
         return f"{self.role} at {self.nom_entreprise}"


class Service(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='services')
    details = models.CharField(max_length=200)
    type_de_service = models.CharField(max_length=100)
    outils = models.CharField(max_length=50)

    def __str__(self):
        return self.details


class PriseDeContact(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='contacts')
    nom = models.CharField(max_length=100)
    objet = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField(blank=True, default='')

    def __str__(self):
        return f"Contact from {self.nom} - {self.objet}"


class ReseauSocial(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='reseaux_sociaux')
    nom_platform = models.CharField(max_length=100)
    lien = models.URLField()

    def __str__(self):
        return self.nom_platform


class Localisation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='localisations')
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    quartier = models.CharField(max_length=100, blank=True)
   

    def __str__(self):
        return f"{self.ville}, {self.pays}"
    

