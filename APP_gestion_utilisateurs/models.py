from django.contrib.auth.models import AbstractUser
from django.db import models




# -----------------CLASSE ANNEE SCOLAIRE---------------------#
class AnneeScolaire(models.Model):
     annee_scolaire = models.CharField(max_length = 9)
     def __str__(self):
          return self.annee_scolaire


# -----------------CLASSE ECOLE---------------------#
class Ecole(models.Model):
     ecole = models.CharField(max_length = 150)
     def __str__(self):
          return self.ecole



# -----------------CLASS CLASSE---------------------#
class Classe(models.Model):
     classe = models.CharField( max_length = 20)
     def __str__(self):
     	return self.classe




# -----------------CLASSE UTILISATEUR---------------------#
class Utilisateur(AbstractUser):
     sexe = [('Homme','Homme'), ('Femme','Femme')]
     genre = models.CharField(choices = sexe, max_length=5)
     ecole = models.ForeignKey(Ecole, blank=True, on_delete=models.PROTECT)
     classe = models.ForeignKey(Classe, blank=True, on_delete=models.PROTECT)
     annee_scolaire = models.ForeignKey(AnneeScolaire,blank=True, on_delete=models.PROTECT)
     telephone = models.CharField(max_length=20)
     emprunt_en_cours = models.BooleanField(default=False)
     def __str__(self):
          return self.username