
from datetime import datetime, date
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from . forms import *
from . models import *



onglet_livre=True


#------------------------HOME----------------------------#
def home_view(request):
     accueil=True
     list_livre=Livre.objects.all()
     context= {'list_livre':list_livre, 'accueil':accueil}
     return render(request, 'livre/home_page.html', context)


#-------------------------------ADD LIVRE---------------------------------
def add_livre_view(request):
     add_livre=True
     form= livreForm()
     message=""
     if request.method == 'POST':
          form = livreForm(request.POST, request.FILES)
          if form.is_valid():
               titre_saisie=form.cleaned_data['titre']
               auteur_choisi=form.cleaned_data['auteur']
               categorie_choisi=form.cleaned_data['auteur']
               
               if Livre.objects.filter(titre=titre_saisie).exists() and Livre.objects.filter(auteur=auteur_choisi).exists() and Livre.objects.filter(categorie=categorie_choisi).exists():
                    message="Cet livre existe déjà."
               else:
                    form.save()
                    return redirect('admin_url')
          else:
               message="Une erreur s'est produit, réessayer."
     return render(request, 'livre/add_livre_page.html', {'form':form, 'message':message, 'onglet_livre':onglet_livre, 'add_livre':add_livre})
     
     
     #-------------------------CATEGORIE---------------------#
def add_categorie_view(request):
     message=""
     form= categorieForm()
     if request.method=="POST":
          form = categorieForm(request.POST)
          if form.is_valid():
               categorie_saisie=form.cleaned_data['categorie']
               if Categorie.objects.filter(categorie=categorie_saisie).exists():
                    message=f"La catégorie \"{categorie_saisie}\" existe déjà."
               else:
                    form.save()
                    return redirect('add_livre_url')
          else:
               message="Erreur d'ajout, réessayer."
     return render(request, 'livre/add_categorie_page.html' , {'form':form, 'message':message })


#-------------------------AUTEUR----------------------#
def add_auteur_view(request):
     message=""
     form= auteurForm()
     if request.method=="POST":
          form=auteurForm(request.POST)
          if form.is_valid():
               auteur_saisie=form.cleaned_data['auteur']
               nationalite_choisi=form.cleaned_data['nationalite']
               if Auteur.objects.filter(auteur=auteur_saisie).exists() and Auteur.objects.filter(nationalite=nationalite_choisi).exists():
                    message=f"L'auteur \"{auteur_saisie}\" existe déjà."
               else:
                    form.save()
                    return redirect('add_livre_url')
          else:
               message="Erreur d'ajout, réessayer."
     return render(request, 'livre/add_auteur_page.html' , {'form':form, 'message':message })


#-------------------------NATIOONALITE----------------------#
def add_nationalite_view(request):
     message=""
     form= nationaliteForm()
     if request.method=="POST":
          form=nationaliteForm(request.POST)
          if form.is_valid():
               nationalite_saisie=form.cleaned_data['nationalite']
               if nationalite.objects.filter(nationalite=nationalite_saisie).exists():
                    message=f"La nationalité \"{nationalite_saisie}\" existe déjà."
               else:
                    form.save()
                    return redirect('add_auteur_url')
          else:
               message="Erreur d'ajout, réessayer."
     return render(request, 'livre/add_nationalite_page.html' , {'form':form, 'message':message })


#---------------------------------ADMIN------------------------

def delete_livre_view(request, pk):
     livre=Livre.objects.get(id=pk)
     livre.delete()
     return redirect('admin_url')


#------------------------ACCUEIL----------------------------#
def abonne_view(request):
     return redirect('accueil')




#------------------------AFFICHE LIVRE----------------------------#
def admin_home_view(request):
     
     admin_page=True
     nombre_de_livre=Livre.objects.count()
     list_livre=Livre.objects.all()
     context= {'list_livre':list_livre, 'admin_page':admin_page, 'onglet_livre':onglet_livre, 'nombre_de_livre':nombre_de_livre}
     return render(request, 'livre/admin_home_page.html', context)



#-------------------------MODIFIER LIVRE--------------------------------------#
class modifier_livre_class(UpdateView):
     model = Livre
     form_class= livreForm
     template_name = "livre/add_livre_page.html"
     success_url= "/admin_url"
     
     
     
#--------------------------------DETAIL LIVRE---------------------------------
def detail_livre_view(request, pk):
     livre_choisi=Livre.objects.get(id=pk)
     cat=livre_choisi.categorie
     aut=livre_choisi.auteur
     aut_id=livre_choisi.auteur_id
     
     auteur_livre=Auteur.objects.get(id=aut_id)
     de_meme_auteur = Livre.objects.filter(auteur=aut).exclude(id=pk)[:3]
     de_meme_categorie = Livre.objects.filter(categorie=cat).exclude(id=pk)[:8]
     context= {'livre_choisi':livre_choisi,'de_meme_auteur':de_meme_auteur ,'de_meme_categorie':de_meme_categorie ,'auteur_livre':auteur_livre,  'onglet_livre':onglet_livre}
     return render(request, 'livre/detail_livre_page.html', context)



#---------------HOME--PRETER LIVRE------------------------------
def home_pret_view(request):
     onglet_pret=True
     nombre_de_pret=Pret.objects.count()
     list_pret=Pret.objects.all()
     context= {'onglet_pret':onglet_pret, 'nombre_de_pret':nombre_de_pret, 'list_pret':list_pret}
     return render(request, 'livre/home_pret_page.html', context)


#--------------------------------------FAIRE UN PRET----------------------------------
def add_pret_view(request):
     onglet_pret=True
     message=""
     form= pretForm()
     if request.method=="POST":
          form = pretForm(request.POST)
          id_livre_choisi=request.POST['livre']
          id_abonne_choisi=request.POST['abonne']
          livre_choisi=Livre.objects.filter(id=id_livre_choisi)
          abonne_choisi=Utilisateur.objects.filter(id=id_abonne_choisi)
          if livre_choisi.exists() and abonne_choisi.exists():
               ancien_exemplaire=livre_choisi[0].exemplaire
               ancien_frequence=livre_choisi[0].frequence
               nouveau_frequence=ancien_frequence+1
               nouveau_exemplaire=ancien_exemplaire-1
               
               if Pret.objects.filter(abonne_id=id_abonne_choisi).exists():
                    message=f"{abonne_choisi[0].last_name} {abonne_choisi[0].first_name} a déjà un emprunt en cours"
               else:
                    if nouveau_exemplaire<0:
                         message=f"Erreur! Il ne reste plus aucun exemplaire du livre \"{livre_choisi[0]}\" "
                    else:
                         abonne_choisi.update(emprunt_en_cours=True)
                         livre_choisi.update(exemplaire=nouveau_exemplaire)
                         livre_choisi.update(frequence=nouveau_frequence)
                         form.save()
                         return redirect('home_pret_url')
          else:
               message="Erreur! Vérifier bien les informations fournies, puis réessayer"
     context={'form':form, 'message':message, 'onglet_pret':onglet_pret}
     return render(request, 'livre/add_pret_page.html' ,context)


#--------------------------------RRETOUR PRET---------------------------------------------------
def retour_pret_view(request,pk):
     pret=Pret.objects.get(id=pk)
     id_livre_choisi= pret.livre_id
     id_abonne_choisi=pret.abonne_id
     livre_choisi=Livre.objects.filter(id=id_livre_choisi)
     abonne_choisi=Utilisateur.objects.filter(id=id_abonne_choisi)
     ancien_exemplaire=livre_choisi[0].exemplaire
     nouveau_exemplaire=ancien_exemplaire+1
     
     abonne_choisi.update(emprunt_en_cours=False)
     livre_choisi.update(exemplaire=nouveau_exemplaire)
     # HistoriquePret.abonne=abonne_choisi.username
     # HistoriquePret.livre=livre_choisi.titre
     # HistoriquePret(abonne=abonne_choisi[0].id, livre=livre_choisi[0].id, date_de_sortie=pret.date_de_sortie)
     # HistoriquePret.save()
     pret.delete()
     return redirect('home_pret_url')



#---------------------MES LIVRE------------------------------------------
@login_required
def mes_livres_view(request):
     if Pret.objects.filter(abonne_id=request.user.id).exists():
          id_abonne_connecter= request.user.id
          pret=Pret.objects.get(abonne_id=id_abonne_connecter)
          id_livre=pret.livre_id
          livre=Livre.objects.get(id=id_livre)
          
          
          delait=pret.delait_de_retour
          now=datetime.now().date()
          temps_restant=int((delait-now).days)
          # temps_restant=
          jour_de_retard=-1*(temps_restant)
          en_retard=False
          j_jour=False
          if temps_restant<0:
               en_retard=True
          elif temps_restant==0:
               j_jour=True   
          context={'pret':pret, 'livre':livre, 'temps_restant':temps_restant, 'jour_de_retard':jour_de_retard, 'en_retard':en_retard, 'j_jour':j_jour}
          return render(request, 'livre/mes_livres.html', context)
     else:
          message="Auncun livre emprunté"
          return render(request, 'livre/mes_livres.html',{'message':message} )
     
     
#------------------------RECHERCHE LIVRE----------------------------------
def recherche_livre_view(request):
     if request.method=="POST":
          accueil=True
          mot=request.POST['mot']
          list_livre_recherche=Livre.objects.filter(titre__contains=mot)
          context={'list_livre':list_livre_recherche, 'accueil':accueil}
     return render(request, 'livre/home_page.html', context)