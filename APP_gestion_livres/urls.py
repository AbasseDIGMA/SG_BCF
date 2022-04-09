from django.urls import path
from .views import *



# ------------------Gestion de livres--URLS--------------
urlpatterns = [
     
     path('accueil',home_view, name='accueil'),
     path('add_livre_url',add_livre_view, name='add_livre_url'),
     path('add_auteur_url',add_auteur_view, name='add_auteur_url'),
     path('add_categorie_url',add_categorie_view, name='add_categorie_url'),
     path('add_nationalite_url',add_nationalite_view, name='add_nationalite_url'),
     path('admin_url',admin_home_view, name='admin_url'),
     path('delete_livre_url/<int:pk>',delete_livre_view, name='delete_livre_url'),
     path('modifier_livre_url/<int:pk>',modifier_livre_class.as_view(), name='modifier_livre_url'),
     path('datail_livre_url/<int:pk>',detail_livre_view, name='detail_livre_url'),
     path('home_pret_url',home_pret_view, name='home_pret_url'),
     path('add_pret_url',add_pret_view, name='add_pret_url'),
     path('retour_pret_url/<int:pk>',retour_pret_view, name='retour_pret_url'),
     path('mes_livres_url',mes_livres_view, name='mes_livres_url'),
     path('recherche_livre_url',recherche_livre_view, name='recherche_livre_url'),
     
]