from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.edit import UpdateView
from . forms import *
from . models import *
import time


onglet_abonne=True

#------------------------CONNEXION------------------------------#
def login_view(request):
     form = LoginForm()
     message=''
     if request.method == 'POST':
          form = LoginForm(request.POST)
          if form.is_valid():
               utilisateur = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
               if utilisateur is not None:
                    login(request, utilisateur)
                    return redirect('home_url')
               else:
                    message = f"Nom ou mot de passe incorrecte"
                    return render(request,'utilisateur/login_page.html', {'form':form, 'message':message})
     return render(request, 'utilisateur/login_page.html', {'form':form})



#---------------------------DECONNEXION------------------------------------#      

def logout_view(request):
     logout(request)
     return redirect('login_url')



#---------------------------INSCRIPTION------------------------------------#

def add_compte_view(request):
     add_abonne=True
     message=""
     form = compteForm()
     if request.method == 'POST':
          form = compteForm(request.POST)
          if form.is_valid():
               
               first_name_saisie=Utilisateur.objects.filter(first_name=form.cleaned_data['first_name']).exists()
               last_name_saisie=Utilisateur.objects.filter(first_name=form.cleaned_data['last_name']).exists()
               username_saisie=Utilisateur.objects.filter(first_name=form.cleaned_data['username']).exists()
               telephone_saisie=Utilisateur.objects.filter(first_name=form.cleaned_data['telephone']).exists()
               genre_choisi=Utilisateur.objects.filter(first_name=form.cleaned_data['genre']).exists()
               ecole_choisi=Utilisateur.objects.filter(first_name=form.cleaned_data['ecole']).exists()
               classe_choisi=Utilisateur.objects.filter(first_name=form.cleaned_data['classe']).exists()
               
               if first_name_saisie and last_name_saisie and username_saisie and telephone_saisie and  genre_choisi and ecole_choisi and classe_choisi:
                    message="Un abonné utilise déjà ces informations."
               else:
                    form.save()
                    return redirect('home_page_abonne_url')
          else:
               message="Une erreur s'est produit , réessayer."
     return render(request, 'utilisateur/add_compte_page.html', {'form':form, 'message':message,'onglet_abonne':onglet_abonne, 'add_abonne': add_abonne} )

#------------------------------CHANGE PASS---------------------------------
def change_pass_view(request):
     message=""
     if request.method=='POST':
          form=PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
               user=form.save()
               update_session_auth_hash(request, user)
               messages.success(request,"Votre mot de passe a été changé avec succès!")
               message="Mot de pass changé avec succès"
               return redirect('confirm_pass_url')
          else:
               messages.error(request, "Erreur de changement de mot de passe!" )
     else:
          form=PasswordChangeForm(request.user)
     return render(request, 'utilisateur/change_pass.html', {'form':form, 'message':message})
     
     
#--------------------------CONFIRM CHANGEMENT---------------------------
def confirm_pass_view(request):
     return render(request, 'utilisateur/confirm_pass_page.html')

#----------------------------INFO--------------------------#
def info_view(request):
     return render(request, 'utilisateur/info_page.html')



#-------------------------AJOIUTER UNE CLASSE----------------------#
def add_classe_view(request):
     message=""
     form= classeForm()
     if request.method=="POST":
          form=classeForm(request.POST)
          if form.is_valid():
               classe_saisie=form.cleaned_data['classe']
               if Classe.objects.filter(classe=classe_saisie).exists():
                    message=f'La classe "{classe_saisie}" existe déjà.'
               else:
                    form.save()
                    return redirect('add_compte_url')
          else:
               message="Erreur d'ajout, réessayer."
     return render(request, 'utilisateur/add_classe_page.html' , {'form':form, 'message':message })



#-------------------------AJOIUTER UNE ECOLE----------------------#
def add_ecole_view(request):
     message=""
     form= ecoleForm()
     if request.method=="POST":
          form=ecoleForm(request.POST)
          if form.is_valid():
               ecole_saisie=form.cleaned_data['ecole']
               if Ecole.objects.filter(ecole=ecole_saisie).exists():
                    message=f"L'école \"{ecole_saisie}\" existe déjà."
               else:
                    form.save()
                    return redirect('add_compte_url')
          else:
               message="Erreur d'ajout, réessayer."
     return render(request, 'utilisateur/add_ecole_page.html' , {'form':form, 'message':message })



#-------------------------AJOIUTER UNE ANNEE_SCOLAIRE----------------------#
def add_annee_scolaire_view(request):
     message=""
     form= annee_scolaireForm()
     if request.method=="POST":
          form=annee_scolaireForm(request.POST)
          if form.is_valid():
               annee_scolaire_saisie=form.cleaned_data['annee_scolaire']
               if AnneeScolaire.objects.filter(annee_scolaire=annee_scolaire_saisie).exists():
                    message=f"L'année scolaire \"{annee_scolaire_saisie}\" existe déjà."
               else:
                    form.save()
                    return redirect('add_compte_url')
          else:
               message="Erreur d'ajout, réessayer."
     return render(request, 'utilisateur/add_annee_scolaire_page.html' , {'form':form , 'message':message })





#------------------------AFFICHE ABONNE----------------------------#
def home_page_abonne_view(request):
     nombre_de_abonne=Utilisateur.objects.count()
     list_abonne=Utilisateur.objects.all()
     context= {'list_abonne':list_abonne,'onglet_abonne':onglet_abonne, 'nombre_de_abonne':nombre_de_abonne}
     return render(request, 'utilisateur/home_page_abonne.html', context)

#-------------------DELETE ABONNE--------------------------------------#
def delete_abonne_view(request, pk):
     abonne=Utilisateur.objects.get(id=pk)
     abonne.delete()
     return redirect('home_page_abonne_url')


#-------------------------MODIFIER PROFILS--------------------------------------#
class modifier_abonne_class(UpdateView):
     model = Utilisateur
     form_class= compteForm
     template_name = "utilisateur/add_compte_page.html"
     success_url= "/home_page_abonne_url"
     
     
     
#--------------------------------DETAIL ABONNE---------------------------------
def detail_abonne_view(request, pk):
     abonne_choisi=Utilisateur.objects.get(id=pk)
     context= {'abonne_choisi':abonne_choisi, 'onglet_abonne':onglet_abonne}
     return render(request, 'utilisateur/detail_abonne_page.html', context)



#--------------------EDIT CARTE-----------------------------------------
def edit_carte_view(request, id):
     abonne=Utilisateur.objects.get(id=id)
     context={'abonne':abonne}
     return render(request, 'utilisateur/edit_carte.html', context)
     

#--------------------------CARTE HOME------------------
def home_carte_view(request):
     onglet_carte=True
     message=""
     if request.method=="POST":
          id=request.POST['num_carte']
          if Utilisateur.objects.filter(id=id).exists():
               url=f"edit_carte_url/{id}"
               return redirect(url)
          else:
               message="Aucun compte associé à ce numero"
     return render(request, 'utilisateur/home_carte_page.html', {'onglet_carte':onglet_carte, 'message':message})
