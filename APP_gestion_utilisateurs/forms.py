from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . models import *


TypeText= forms.TextInput(attrs={'class':'form-control'})
TypeTexarea= forms.Textarea(attrs={'class':'form-control'})
TypeNumber= forms.NumberInput(attrs={'class':'form-control', 'min':'0'})
TypeEmail= forms.EmailInput(attrs={'class':'form-control'})
TypePass= forms.PasswordInput(attrs={'class':'form-control', 'value':'1234'})
TypeCheckbox= forms.CheckboxInput(attrs={'class':'form-check-input'})
TypeSelect= forms.Select(attrs={'class':'form-control'})



# -----------------formulaire de connexion-----------------------
class LoginForm(forms.Form):  
    Text = forms.TextInput(attrs={'class':'form-control'})
    Password = forms.PasswordInput(attrs={'class':'form-control'})
    
    username = forms.CharField(max_length=100, widget=Text)
    password = forms.CharField(max_length=100, widget= Password)
    
    
    
    
# -----------------formulaire de creation de copmpte-----------------------
class compteForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
            model = Utilisateur
            fields = ('first_name', 'last_name', 'username','ecole','classe','annee_scolaire', 'genre','telephone','email', 'is_staff')
            widgets ={
                'first_name':TypeText,
                'last_name':TypeText,
                'username':TypeText,
                'ecole':TypeSelect,
                'classe':TypeSelect,
                'annee_scolaire':TypeSelect,
                'genre':TypeSelect,
                'telephone':TypeNumber,
                'email':TypeEmail,
                'is_staff':TypeCheckbox,
            
             }


#---------------------FORM CLASSE----------------------------------#
class classeForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = {'classe'}
        widgets = {
            'classe':TypeText,
        }


#---------------------FORM ECOLE----------------------------------#
class ecoleForm(forms.ModelForm):
    class Meta:
        model = Ecole
        fields = {'ecole'}
        widgets = {
            'ecole':TypeText,
        }

#---------------------FORM ANNEE_SCOLAIRE----------------------------------#
class annee_scolaireForm(forms.ModelForm):
    class Meta:
        model = AnneeScolaire
        fields = {'annee_scolaire'}
        widgets = {
            'annee_scolaire':TypeText,
        }
