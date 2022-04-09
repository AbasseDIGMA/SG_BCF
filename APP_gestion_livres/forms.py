from django import forms
from APP_gestion_utilisateurs.models import *
from APP_gestion_livres.models import *


TextType= forms.TextInput(attrs={'class':'form-control'})
TextareaType= forms.Textarea(attrs={'class':'form-control'})
NumberType= forms.NumberInput(attrs={'class':'form-control', 'min':'0'})
SelectType= forms.Select(attrs={'class':'form-control'})

        
class livreForm(forms.ModelForm):
    class Meta():
        model = Livre
        fields = ["titre", "image", "auteur", "categorie", "desc", "exemplaire"]


        #---------------LES TYPE HTML AVEC DES CLASSE BOOTSTRAPE-------------------#

        widgets = {
            'titre':TextType,
            'auteur':SelectType,
            'categorie':SelectType,
            'desc':TextareaType,
            'exemplaire':NumberType,
            # 'ISBN':NumberType,
        }



#---------------------FORM CATEGORIE----------------------------------#
class categorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = {'categorie'}
        widgets = {
            'categorie':TextType,
        }




#---------------------FORM AUTEUR----------------------------------#
class auteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = {'auteur', 'nationalite', 'desc'}
        widgets = {
            'auteur':TextType,
            'nationalite':SelectType,
            'desc':TextareaType,
        }


#---------------------FORM nationalite----------------------------------#
class nationaliteForm(forms.ModelForm):
    class Meta:
        model = nationalite
        fields = {'nationalite'}
        widgets = {
            'nationalite':TextType,
        }
        
        
class pretForm(forms.ModelForm):
    class Meta:
        model = Pret
        fields= {'abonne', 'livre'}
        widgets={
            'abonne':NumberType,
            'livre':NumberType
        }