from .models import *

import django_filters
from django_filters import DateFilter, CharFilter,ChoiceFilter

class DepartFilters(django_filters.FilterSet):
    nom = CharFilter(field_name='nom_departement', lookup_expr='icontains')
    code = CharFilter(field_name='code_departement', lookup_expr='icontains')

    class Meta:
        model = Departement
        fields = ['nom_departement', 'code_departement']
        exclude = ['nom_departement', 'code_departement']

class MatiereFilters(django_filters.FilterSet):
    code = CharFilter(field_name='code_matiere', lookup_expr='icontains')


    class Meta:
        model = Matiere
        fields = ['niveau']
        #exclude = ['coefficient_matiere', 'nom_matiere','nature_ue','horaire',  'specialite', ' filMatiere','niveau']

class FiliereFilters(django_filters.FilterSet):
    nom = CharFilter(field_name='nom_filiere', lookup_expr='icontains')
    code = CharFilter(field_name='code_filiere', lookup_expr='icontains')


    class Meta:
        model =Filiere
        fields = '__all__'
        exclude = ['nom_filiere', 'code_filiere']
        

class EtudiantFilter(django_filters.FilterSet):
    class Meta:
        model = Etudiant
        fields = ['semestre', 'filiere']
       