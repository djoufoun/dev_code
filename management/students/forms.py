from django.forms import ModelForm, forms, Field, widgets
from django import forms
from .models import *



class AnneeForm(ModelForm):
    class Meta:
        model = anneeScolaire
        fields = '__all__'

        widgets = {
            'anneescolaire': forms.TextInput(attrs={'class':'form-control', 'placeholder':'annee scolaire'}),
            'annee_debut': forms.TextInput(attrs={'class':'form-control',  'type':'date'}),
            'annee_fin':forms.TextInput(attrs={'class':'form-control', 'type':'date'})
        }

class DepartementForm(ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'

        widgets = {
            'nom_section_sco': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer nom du section scolaire'}),
            'code_section_sco': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer code du section scolaire'})
        }

class filiereForm(ModelForm):
    class Meta:
        model = Filiere
        fields = '__all__'

        widgets = {
            'nom_filiere':forms.Select(attrs={'class':'form-control', 'placeholder':'Entrer nom du Filiere'}),
            'code_filiere':forms.Select(attrs={'class':'form-control', 'placeholder':'Entrer code du Filiere'}),
            'id_departement':forms.Select(attrs={'class':'form-control',})
      
      
        }

#----------------------------Matiere Form ----------------------------------------------
class matiereForm(ModelForm):
    class Meta:
        model = Matiere
        fields = '__all__'

        widgets = {
            'nom_matiere':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer nom du Matière'}),
            'code_matiere':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer code du matière'}),
            'nature_ue':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer nnature de le matière'}),
            'code_ue':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer code du nature'}),
            'coefficient_matiere':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer coefficient du matière', 'type':'number'}),
            'horaire':forms.TextInput(attrs={'class':'form-control','placeholder':'Entrer volume horaire du matière' ,'type':'number'}), 
            'filMatiere':forms.SelectMultiple(attrs={'class':'form-control'}), 
            'filMatiere':forms.SelectMultiple(attrs={'class':'form-control'}), 
            'niveau':forms.Select(attrs={'class':'form-control',  'type':'number'}),
            'semestre':forms.Select(attrs={'class':'form-control'}),
            'specialite':forms.SelectMultiple(attrs={'class':'form-control'})   
     
        }


#----------------------------classRoom Form ----------------------------------------------
class classRoomForm(ModelForm):
    class Meta:
        model = ClassRoom
        fields = '__all__'

        widgets = {
            'nom_classe':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer nom du Matière'}),
            'code_classe':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer code du matière'}),
        }



#----------------------------End Matiere Form ----------------------------------------------

class specialiteForm(ModelForm):
    class Meta:
        model = Specialite
        fields = '__all__'

        widgets = {
            'nom_specialite':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer nom de Specialité'}),
            'code_specialite':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer code du Specialité'}),
            'filiere':forms.Select(attrs={'class':'form-control' }),
        }
#----------------------------End Specialité Form ----------------------------------------------



class niveauForm(ModelForm):
    class Meta:
        model = Niveau
        fields = '__all__'

        widgets = {
            'nom_niveau':forms.Select(attrs={'class':'form-control' }),
            'code_niveau':forms.Select(attrs={'class':'form-control'}),
            'anneeScolaire':forms.Select(attrs={'class':'form-control' }),
        }
    
#----------------------------End Niveau Form ----------------------------------------------



class semestreForm(ModelForm):
    class Meta:
        model = Semestre
        fields = '__all__'

        widgets = {
            'nom_semestre':forms.Select(attrs={'class':'form-control', 'placeholder':'Entrer nom de Specialité'}),
            'code_semestre':forms.Select(attrs={'class':'form-control', 'placeholder':'Entrer code du Specialité'}),
            }
    
#----------------------------End Semestre Form ----------------------------------------------


class studentForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'
        exclude = ['id_etudiant']
        widgets = {
            'id_etudiant':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer ID de Etudiant'}),
            'nom':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer nom etudiant'}),
            'prenom':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer prénom etudiant'}),
            'specialite':forms.SelectMultiple(attrs={'class':'form-control'}),
            'date_naissance':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer prénom etudiant', 'type':'date'}),
            }
    
#----------------------------End Student Form ----------------------------------------------



class tuteurForm(ModelForm):
    class Meta:
        model = Tuteur
        fields = '__all__'

        widgets = {
            'nom':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer nom du tuteur'}),
            'prenom':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer prénom du tuteur'}),
            'date_naissance':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer date de naissance', 'type':'date'}),
            'telephone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer numero de telephone du tuteur', 'type':'number'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer email du tuteur', 'type':'email'}),
            'adresse':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer adresse du tuteur'}),
            'adresse':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer adresse du tuteur'}),
            'adresse_physique':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer adresse physique'}),
            
            
            }
    
#----------------------------End Tuteur Form ----------------------------------------------



class teacherForm(ModelForm):
    class Meta:
        model = Enseignant
        fields = '__all__'

        widgets = {
            'nom':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer nom etudiant'}),
            'prenom':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer prénom etudiant'}),
            'date_naissance':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer prénom etudiant', 'type':'date'}),
            'telephone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer numero etudiant', 'type':'number'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer eemail etudiant', 'type':'email'}),
            'adresse':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer adresse etudiant'}),
            
            }
    
#----------------------------End Teachers Form ----------------------------------------------

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

        widgets = {
            'type_note':forms.TextInput(attrs={'class':'form-control'}),
            'matiere':forms.TextInput(attrs={'class':'form-control', }),
            'etudiant':forms.TextInput(attrs={'class':'form-control', }),
            'note':forms.TextInput(attrs={'class':'form-control',  'type':'number'})
            
            }
        
class EmploisForm(ModelForm):
    class Meta:
        model = Emplois
        fields = '__all__'

        widgets = {
            'type_emplois':forms.Select(attrs={'class':'form-control'}),
            'annee':forms.Select(attrs={'class':'form-control'}),
            'date':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'status':forms.Select(attrs={'class':'form-control', }),
            'niveau':forms.Select(attrs={'class':'form-control', }),
            'semestre':forms.Select(attrs={'class':'form-control'}),
            'matiere':forms.Select(attrs={'class':'form-control',}),
            'enseignant':forms.Select(attrs={'class':'form-control'}),
            'classe':forms.Select(attrs={'class':'form-control'}),
            
            }
        

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'annee_universitaire':forms.Select(attrs={'class':'form-control',}),
            'date_du_jour':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'commentaire':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Laissez vos communiqués ici !'}),   
            }