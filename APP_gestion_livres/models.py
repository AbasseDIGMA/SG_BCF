from django.db import models
from django.conf import settings
from datetime import date, timedelta
from APP_gestion_utilisateurs.models import Utilisateur

#------------------------------CLASS CATEGORIE-----------------------------#
class Categorie(models.Model):
     categorie = models.CharField(max_length=50)
     def __str__(self):
          return self.categorie


#------------------------------CLASS nationalite-----------------------------#
class nationalite(models.Model):
     nationalite = models.CharField(max_length=50)
     def __str__(self):
          return self.nationalite


#------------------------------CLASS AUTEUR-----------------------------#
class Auteur(models.Model):
     auteur = models.CharField(max_length=50)
     nationalite = models.ForeignKey(nationalite, on_delete=models.PROTECT, blank=True)
     desc = models.TextField(blank=True)
     def __str__(self):
          return self.auteur    


#------------------------------CLASS LIVRE-----------------------------#
class Livre(models.Model):
     ISBN = models.IntegerField(blank=True, null=True)
     titre = models.CharField( max_length=100)
     image = models.ImageField(null=True, blank=True)
     auteur = models.ForeignKey(Auteur, on_delete=models.PROTECT)
     categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT)
     desc = models.TextField(blank=True)
     exemplaire = models.IntegerField()
     frequence = models.BigIntegerField(default=0)
     creer_le = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return self.titre
     
     
     
#------------------------------CLASS EEMPRUNT-----------------------------#
class Pret(models.Model):
     today = date.today()
     retour = today+timedelta(days=14) #calcul du delai de retour
     abonne = models.ForeignKey(Utilisateur, on_delete=models.PROTECT)
     livre = models.ForeignKey(Livre, on_delete=models.PROTECT)
     date_de_sortie = models.DateTimeField(auto_now_add=True)
     delait_de_retour = models.DateField( default=retour)
     def __str__(self):
          return self.livre
     
class HistoriquePret(models.Model):
     abonne = models.CharField( max_length=50)
     livre = models.CharField( max_length=50)
     date_de_sortie = models.DateTimeField()
     date_d_entree = models.DateTimeField(auto_now_add=True)
     def __str__(self):
          return self.livre