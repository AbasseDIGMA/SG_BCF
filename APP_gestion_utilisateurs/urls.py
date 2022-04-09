from django.urls import path
from .views import *



# ------------------Gestion de utilisateur URLS----------------
urlpatterns = [
     path('login_url',login_view, name='login_url'),
     path('logout_url',logout_view, name='logout_url'),
     path('add_compte_url',add_compte_view, name='add_compte_url'),
     path('change_pass_url',change_pass_view, name='change_pass_url'),
     path('add_info_url',info_view, name='info_url'),
     path('add_ecole_url',add_ecole_view, name='add_ecole_url'),
     path('add_annee_scolaire_url',add_annee_scolaire_view, name='add_annee_scolaire_url'),
     path('add_classe_url',add_classe_view, name='add_classe_url'),
     path('home_page_abonne_url',home_page_abonne_view, name='home_page_abonne_url'),
     path('delete_abonne_url/<int:pk>',delete_abonne_view, name='delete_abonne_url'),
     path('detail_abonne_url/<int:pk>',detail_abonne_view, name='detail_abonne_url'),
     path('modifier_abonne_url/<int:pk>',modifier_abonne_class.as_view(), name='modifier_abonne_url'),
     path('edit_carte_url/<int:id>',edit_carte_view, name='edit_carte_url'),
     path('home_carte_url', home_carte_view, name='home_carte_url'),
     path('confirm_pass_url', confirm_pass_view, name='confirm_pass_url'),


]