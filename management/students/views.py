from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import *
from .models import *
from students.filters import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime

# Create your views here.


def pageaccueil(request):

    student = Etudiant.objects.all()
    student_count = student.count()

    note = Note.objects.all()
    emplois = Emplois.objects.all()

    note_count = note.count()
    emplois_count = emplois.count()
   
    dawm = student.filter(filiere__code_filiere__icontains="dawm").count()
    asrs = student.filter(filiere__code_filiere__icontains="asrs").count()
    annee = anneeScolaire.objects.all().count()
    matiere = Matiere.objects.all().count()
    tuteur = Tuteur.objects.all().count()
    departement = Departement.objects.all().count()
    filiere = Filiere.objects.all().count()
    enseignant = Enseignant.objects.all().count()
    niveau = Niveau.objects.all().count()
    semestre = Semestre.objects.all().count()
    specialite = Specialite.objects.all().count()
    classe = ClassRoom.objects.all().count()
   


    context = {'matiere':matiere,
                'student':student, 'student_count':student_count,'dawm':dawm,"asrs":asrs, 
               'annee':annee, 'tuteur':tuteur, 'departement':departement,'filiere':filiere, 'enseignant':enseignant,
               'niveau':niveau, 'semestre':semestre, 'specialite':specialite, 'classe':classe, 'note_liste':note_count, 'emplois_liste':emplois_count}
    return render(request, 'roles/accueil.html', context)
  


def search_all(request):
    search = request.GET.get('search')
    search_departement = Departement.objects.filter(nom_departement__icontains=search)
    
    context = {'departement':search_departement}
    return render(request, 'search/departement.html', context)


def counter(request):
    annee = anneeScolaire.objects.all().count()
    matiere = Matiere.objects.all()
    mat = matiere.count()
    student = Etudiant.objects.all().count()
    filiere = Filiere.objects.all().count()
  
    context = {'scolaire':annee, 'matiere':mat, 'student':student, 'filiere':filiere}
    return render(request, 'elements/sidebody.html', context)

#------------------------------------Add Annee Scolaire ----------------------------------

def Anneescolaire(request):
    form = AnneeForm()
    if request.method == "POST":
        form = AnneeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'enregistrement est faite avec succée")
            form = AnneeForm()
        else:
            messages.error("l'enregistrement échoué!")
    view_annee = anneeScolaire.objects.all()
    return render(request, 'corps/anneeform.html', {'form':form, 'view_annee':view_annee})

def anneeUpdate(request, pk=None):
    if not pk is None:
        query = anneeScolaire.objects.get(id=pk)
        form = AnneeForm(instance=query)
        if request.POST:
            form = AnneeForm(request.POST, instance=query)
            if form.is_valid():
                form.save()
                messages.success(request, 'La mise à jour des données est faite avec succée')
                return redirect('/anneescolaire')
            else:
                form = AnneeForm()
               
       
    
    return render(request, 'corps/anneeUpdate.html', {'form':form})

def anneeDelete(request, pk=None):
    if not pk is None:
        query = anneeScolaire.objects.get(id=pk)
        data = query.anneescolaire
        if request.POST:            
            query.delete()
            messages.success(request, 'Le donnée été supprimé avec succée')
            return redirect('/anneescolaire')
    return render(request, 'corps/anneeDelete.html', {'data':data})

#--------------------------------------Add Departement ------------------------------------
def Departements(request):
    form = DepartementForm()
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            form = DepartementForm()
            messages.success(request, 'Le departement est enregistré avec succée!')
        else:
            messages.error(request, form.errors)
            form = DepartementForm()
    
    element = Departement.objects.all()

    #filters products
    depart_filters = DepartFilters(request.GET, queryset=element)
    element = depart_filters.qs

    #pagination 
    paginator = Paginator(element, 6)
    page_number = request.GET.get('page')
    departement = paginator.get_page(page_number)
 
    context = {'form':form,  'departement':departement, 'filter':depart_filters}
    return render(request, 'corps/addepartement.html', context)    




#-------Update-------------------
def updateDepartement(request, id):
    element = Departement.objects.get(id=id)
    form = DepartementForm(instance=element)
    if request.method == "POST":
        form = DepartementForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            form = DepartementForm()
            messages.success(request, 'la modification à été bien faite !')
            return redirect('students:departement')
    return render(request, 'corps/updatedepartement.html', {'form':form})

#------------delete---------------
def deleteDepartement(request, id):
    element = Departement.objects.get(id=id)
    obj = element.nom_section_sco
    if request.method == "POST":
        element.delete()
        return redirect('students:departement')
    return render(request, 'corps/deleteDepartement.html', {'obj':obj})
#--------------------------------------end Departement --------------------------------------------


#--------------------------------------Filiere --------------------------------------------
def addFiliere(request):
    form = filiereForm()
    if request.method == "POST":
        form = filiereForm(request.POST)
        if form.is_valid():
            form.save()
            form = filiereForm()
            messages.success(request, 'Enregistrement de filiere est faite avec succée!')
        else:
            messages.error(request, form.errors)

    filiere_list = Filiere.objects.all()
    filcount = filiere_list.count()
    #filters
    filiere_filters = FiliereFilters(request.GET, queryset=filiere_list)
    filiere_list = filiere_filters.qs
    

    #pagination
    paginator = Paginator(filiere_list, 6)
    page_number = request.GET.get('page')
    filiere = paginator.get_page(page_number)
    context = {'form':form, 'filiere':filiere, 'filiere_filters':filiere_filters, 'fil':filcount}

    return render(request, 'corps/addFiliere.html', context)
        
#-------Update filiere-------------------
def updateFiliere(request, id):
    element = Filiere.objects.get(id=id)
    form = filiereForm(instance=element)
    if request.method == "POST":
        form = filiereForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            form = filiereForm()
            messages.success(request, 'la modification à été bien faite !')
            return redirect('students:addfiliere')
    return render(request, 'corps/filiereUpdate.html', {'form':form})

#------------delete Filiere---------------
def deleteFiliere(request, id):
    element = Filiere.objects.get(id=id)
    obj = element.nom_filiere
    if request.method == "POST":
        element.delete()
        return redirect('students:addfiliere')
    return render(request, 'corps/filiereDelete.html', {'obj':obj})

#-------------------------------endFiliere------------------------------------------------

#-------------------------------Niveau------------------------------------------------
def addNiveau(request):
    form = niveauForm()
    if request.method == "POST":
        form = niveauForm(request.POST)
        if form.is_valid():
            form.save()
            form = niveauForm()
            messages.success(request, 'Enregistrement de filiere est faite avec succée!')
        else:
            messages.error(request, form.errors)

    niveau_list = Niveau.objects.all()
    paginator = Paginator(niveau_list, 6)
    page_number = request.GET.get('page')
    niveau = paginator.get_page(page_number)
    context = {'form':form,   'niveau':niveau}

    return render(request, 'corps/niveauAdd.html', context)
        
#-------Update Niveau-------------------
def updateNiveau(request, id):
    element = Niveau.objects.get(id=id)
    form = niveauForm(instance=element)
    if request.method == "POST":
        form = niveauForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            form = niveauForm()
            messages.success(request, 'la modification à été bien faite !')
            return redirect('students:niveau')
    return render(request, 'corps/niveauUpdate.html', {'form':form})

#------------delete Niveau---------------
def deleteNiveau(request, id):
    element = Niveau.objects.get(id=id)
    obj = element.nom_niveau
    if request.method == "POST":
        element.delete()
        return redirect('students:niveau')
    return render(request, 'corps/niveauDelete.html', {'obj':obj})



#-------------------------------endNiveaux------------------------------------------------


#-------------------------------Matiere------------------------------------------------
def addMatiere(request):
    form = matiereForm()
    if request.method == "POST":
        form = matiereForm(request.POST)
        if form.is_valid():
            form.save()
            form = matiereForm()
            messages.success(request, 'Enregistrement de la matière est faite avec succée!')
        else:
            messages.error(request, form.errors)
    
    matiere_list = Matiere.objects.all()

    mat_filters = MatiereFilters(request.GET, queryset=matiere_list)
    matiere_list = mat_filters.qs

    paginator = Paginator(matiere_list, 6)
    page_number = request.GET.get('page')
    matiere = paginator.get_page(page_number)
    
    context = {'form':form,  'matiere':matiere, 'mat_filters':mat_filters}

    return render(request, 'corps/matiereAdd.html', context)
        
#-------Update Matiere-------------------
def updateMatiere(request, id):
    element = Matiere.objects.get(id=id)
    form = matiereForm(instance=element)
    if request.method == "POST":
        form = matiereForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            form = matiereForm()
            messages.success(request, 'la modification à été bien faite !')
            return redirect('students:addmatiere')
    return render(request, 'corps/matiereUpdate.html', {'form':form, })

#------------delete Matiere---------------
def deleteMatiere(request, id):
    element = Matiere.objects.get(id=id)
    obj = element.nom_matiere
    if request.method == "POST":
        element.delete()
        return redirect('students:addmatiere')
    return render(request, 'corps/matiereDelete.html', {'obj':obj})

def showMatiere(request, pk=None):
    context = {}
    if not pk is None:
        data = Matiere.objects.get(id=pk)
        liste_matiere = Matiere.objects.all()
        specialite = data.specialite.all()
        fil_mat = data.filMatiere.all()
        
        context = {'matiere':data, 'liste_matiere':liste_matiere, 'specialite':specialite, 'filiere':fil_mat }
    else:
        context['matiere']={}
   
    return render(request, 'corps/matiereShow.html', context)

#-------------------------------endMatiere------------------------------------------------

#-------------------------------ClasseRoom------------------------------------------------

def addclassRoom(request):
    form = classRoomForm()
    if request.method == "POST":
        form = classRoomForm(request.POST)
        if form.is_valid():
            form.save()
            form = classRoomForm()
            messages.success(request, 'Enregistrement de la classe est faite avec succée!')
        else:
            messages.error(request, form.errors)

    classe_list = ClassRoom.objects.all()
    paginator = Paginator(classe_list, 6)
    page_number = request.GET.get('page')
    classe = paginator.get_page(page_number)
    context = {'form':form,  'classe':classe}

    return render(request, 'corps/classeAdd.html', context)
        
#-------Update Matiere-------------------
def updateclasseRoom(request, id):
    element = ClassRoom.objects.get(id=id)
    form = classRoomForm(instance=element)
    if request.method == "POST":
        form = classRoomForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            form = classRoomForm()
            messages.success(request, 'la modification à été bien faite !')
            return redirect('students:addclasse')
    return render(request, 'corps/classeUpdate.html', {'form':form,})

#------------delete Matiere---------------
def deleteclasseRoom(request, id):
    element = ClassRoom.objects.get(id=id)
    obj = element.nom_classe
    if request.method == "POST":
        element.delete()
        return redirect('students:addclasse')
    return render(request, 'corps/classeDelete.html', {'obj':obj})
#-------------------------------EndClasseRoom------------------------------------------------


#-------------------------------EndClasseRoom------------------------------------------------
def specialite(request):
    form = specialiteForm()
    if request.method == "POST":
        form = specialiteForm(request.POST)
        if form.is_valid():
            form.save()
            form = specialiteForm()
            messages.success(request, 'Enregistrement de la spécialité est faite avec succée!')
            return redirect('students:specialite')
        else:
            messages.error(request, form.errors)

    specialite_list = Specialite.objects.all()
    paginator = Paginator(specialite_list, 6)
    page_number = request.GET.get('page')
    specialite = paginator.get_page(page_number)
    context = {'form':form,  'specialite':specialite}

    return render(request, 'corps/specialiteAdd.html', context)
    
#-----------------Update

def updateSpecialite(request, id):
    element = Specialite.objects.get(id=id)
    form = specialiteForm(instance=element)
    if request.method == "POST":
        form = specialiteForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            form = specialiteForm()
            messages.success(request, 'la modification à été bien faite !')
            return redirect('students:specialite')
    return render(request, 'corps/specialiteUpdate.html', {'form':form})

#-----------------Delete

def deleteSpecialite(request, id):
    element = Specialite.objects.get(id=id)
    obj = element.nom_specialite
    if request.method == "POST":
        element.delete()
        return redirect('students:specialite')
    return render(request, 'corps/specialiteDelete.html', {'obj':obj})

#-------------------------------EndSpecialite------------------------------------------------


#-------------------------------Semestre------------------------------------------------
def addSemestre(request):
    form = semestreForm()
    if request.method == "POST":
        form = semestreForm(request.POST)
        if form.is_valid():
            form.save()
            form = semestreForm()
            messages.success(request, 'Enregistrement de semestre est faite avec succée!')
            return redirect('students:semestre')
        else:
            messages.error(request, form.errors)

    semestre_list = Semestre.objects.all()
    paginator = Paginator(semestre_list, 6)
    page_number = request.GET.get('page')
    semestre = paginator.get_page(page_number)
    context = {'form':form,  'semestre':semestre}

    return render(request, 'corps/semestreAdd.html', context)
    
#-----------------Update

def updateSemestre(request, id):
    element = Semestre.objects.get(id=id)
    form = semestreForm(instance=element)
    if request.method == "POST":
        form = semestreForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            form = semestreForm()
            messages.success(request, 'la modification à été bien faite !')
            return redirect('students:semestre')
    return render(request, 'corps/semestreUpdate.html', {'form':form})

#-----------------Delete

def deleteSemestre(request, id):
    element = Semestre.objects.get(id=id)
    obj = element.nom_semestre
    if request.method == "POST":
        element.delete()
        messages.success(request, 'la suppression de semestre est fait avec succèes')           
                       
        return redirect('students:semestre')
    return render(request, 'corps/semestreDelete.html', {'obj':obj})

#-------------------------------EndSpecialite------------------------------------------------


#-------------------------------Etudiants------------------------------------------------
def addStudent(request):
    form = studentForm()
    if request.method == "POST":
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            current_year = datetime.date.today().year
            id_etudiant = Etudiant.objects.all().count()+1
            matricule = str("AMDJ")+ str(current_year)+"-"+str(id_etudiant)
            student.id_etudiant = matricule
            student.save()
            form = studentForm()
            messages.success(request, 'Enregistrement de étudiant est faite avec succée!')
            return redirect('students:student')
        else:
            messages.error(request, form.errors)

    student_list = Etudiant.objects.all()
    paginator = Paginator(student_list, 6)
    page_number = request.GET.get('page')
    student = paginator.get_page(page_number)
    context = {'form':form,  'student':student}

    return render(request, 'personels/studentAdd.html', context)
    
#-----------------Update

def studentUpdate(request, id):
    element = Etudiant.objects.get(id=id)
    form = studentForm(instance=element)
    if request.method == "POST":
        form = studentForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            form = studentForm()
            messages.success(request, 'la modification à été bien faite !')
            return redirect('students:student')
    return render(request, 'personels/studentUpdate.html', {'form':form})

#-----------------Delete

def studentDelete(request, id):
    element = Etudiant.objects.get(id=id)
    obj = element.nom + " "+ element.prenom
    if request.method == "POST":
        element.delete()
        return redirect('students:student')
    return render(request, 'personels/studentDelete.html', {'obj':obj})

#------student show

def studentShow(request, pk= None):
    context = {}
    if not pk is None:
        data = Etudiant.objects.get(id=pk)
        student = Etudiant.objects.all()
        context['views_stud'] = data
        context['all_student'] = student
    else:
        context['views_stud']= {}

    return render(request, 'personels/studentShow.html', context)
#-------------------------------EndStudent------------------------------------------------



#-------------------------------Tuteur------------------------------------------------

def tuteurAdd(tuteur):
    form = tuteurForm()
    if tuteur.method == "POST":
        form = tuteurForm(tuteur.POST, tuteur.FILES)
        if form.is_valid():
            form.save()
            form = tuteurForm()
            messages.success(tuteur, 'le données sont enregistrées avec succées!')
            return redirect('students:tuteur')
        else:
            messages.error(tuteur, 'Erreur!')

    tuteur_list = Tuteur.objects.all()
    paginator = Paginator(tuteur_list, 6)
    page_number = tuteur.GET.get('page')
    tuteurs = paginator.get_page(page_number)
    context = {'form':form, 'tuteurs':tuteurs}

    return render(tuteur, 'personels/tuteurAdd.html', context)


#-------------------------Update Tuteur-----


def tuteurUpdate(tuteur, id):
    element = Tuteur.objects.get(id=id)
    form = tuteurForm(instance=element)
    if tuteur.method == "POST":
        form = tuteurForm(tuteur.POST, instance=element)
        if form.is_valid():
            form.save()
            messages.success(tuteur, 'la modification à été faite avec succées!')
            return redirect('students:tuteur')
    return render(tuteur, 'personels/tuteurUpdate.html', {'form':form})    

#------------------------Delete Tuteur


def tuteurDelete(tuteur, id):
    element = Tuteur.objects.get(id=id)
    obj = element.nom +" "+ element.prenom
    if tuteur.method == "POST":
        element.delete()
        return redirect('students:tuteur')
    
    return render(tuteur, 'personels/tuteurDelete.html', {'obj':obj})

#------------------------tuteur show
def tuteurShow(request, pk=None):
    context = {}
    if not pk is None:
        all_tuteur = Tuteur.objects.all()
        data = Tuteur.objects.get(id=pk)
        student = data.etudiant_set.all()
        
        context = {'tuteur':data, 'student':student, 'all_tuteur':all_tuteur}
    else:
        context['tuteur']={}
    return render(request, 'personels/tuteurShow.html', context)

#-------------------------------EndTuteur--------------------------------------------



def teacherAdd(request):
    form = teacherForm()
    if request.method == "POST":
        form = teacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = teacherForm()
            messages.success(request, 'le données sont enregistrées avec succées!')
            return redirect('students:teacherAdd')
        else:
            messages.error(request, 'Erreur!')

    teacher_list = Enseignant.objects.all()
    paginator = Paginator(teacher_list, 6)
    page_number = request.GET.get('page')
    teacher = paginator.get_page(page_number)
    context = {'form':form, 'teacher':teacher}

    return render(request, 'personels/teacherAdd.html', context)


def teacherUpdate(request, pk=None):

    if not pk is None:
        data = Enseignant.objects.get(id=pk)
        form = teacherForm(instance=data)
        if request.method=="POST":
            form = teacherForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                form = teacherForm()
                messages.success(request, 'la modification est faite avec success')
                return redirect('/teacherAdd')
            else:
                messages.error(request, 'Erreur!')
    else:
        messages.error(request, 'problème de id')
    
    return render(request, 'personels/teacherUpdate.html', {'form':form})

def teacherDelete(request, pk):
    if not pk is None:
        query = Enseignant.objects.get(id=pk)
        element = query.nom +"  "+ query.prenom 
        if request.POST:
            query.delete()
            messages.success(request, 'La suppression à éffectuée avec succée!')
            return redirect('/teacherAdd')          
    
    return render(request, 'personels/teacherDelete.html', {'element':element})



def teacherShow(request, pk=None):
    context = {}
    if not pk is None:
        query = Enseignant.objects.get(id=pk)
        data = Enseignant.objects.all()
        context = {'teacher':query, 'data':data} 
        
    else:
        context={}
        messages.error(request, 'Une erreur est commise!')
    return render(request, 'personels/teacherShow.html', context)


#-------------------------------End Teacher function----------------------------------
#La fonction qui permet de entrer les notes par administrateur
def admin_add_note(request):
    matieres = Matiere.objects.all()
    etudiants = Etudiant.objects.all()
    liste = Note.objects.all()

    if request.method=='POST':
        for  etudiant in etudiants:
            for matiere in matieres:
                for note in request.POST.getlist(f'etudiant_{etudiant.id}_matiere_{matiere.id}'):
                    if not note:
                        continue
                    else:
                        Note.objects.get_or_create(etudiant=etudiant, matiere=matiere, note=note)           
                        
    notes = Note.objects.all()
  
    context = {'etudiants':etudiants, 'matieres':matieres,'all':liste, 'notes':notes}
    return render(request, 'roles/admin_note.html', context)

def teacher_add_note(request):
    matieres = Matiere.objects.all()
    etudiants = Etudiant.objects.all()
    liste = Note.objects.all()

    type_notes = request.POST.get('type_note')

    if request.method=='POST':
        for  etudiant in etudiants:
            for matiere in matieres:
                for note in request.POST.getlist(f'etudiant_{etudiant.id}_matiere_{matiere.id}'):
                    if not note:
                        continue
                    else:
                        Note.objects.get_or_create(etudiant=etudiant, matiere=matiere, note=note, type_note=type_notes)
                        messages.success(request, 'Enregistrement des notes sont faites avec succèes')           
                        
    notes = Note.objects.all()
    views_comment = Comment.objects.all()

    #Filter field
    myFilters = MatiereFilters(request.GET, queryset=matieres)
    matieres = myFilters.qs

    myEtudiants = EtudiantFilter(request.GET, queryset=etudiants)
    etudiants = myEtudiants.qs

  
    context = {'etudiants':etudiants, 'matieres':matieres,'all':liste, 
               'notes':notes, 'filterMatiere':myFilters, 
               'filterEtudiant':myEtudiants, 'views_comment':views_comment}
    return render(request, 'comptes/teacher.html', context)


def UpdateNote(request, pk=None):

    if not pk is None:
        data = Note.objects.get(id=pk)
        form = NoteForm(instance=data)
        if request.method == "POST":
            form = NoteForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                messages.success(request, 'La modification de cette note est faite avec succèe')                 
                return redirect('students:teacher_add_note') 
            else:
                form = NoteForm()
    context ={'form':form}

    return render(request, 'resultats/noteUpdate.html', context)


def NoteDelete(request, pk=None):
    if not pk is None:
        query = Note.objects.get(id=pk)
        if request.POST:
            query.delete()
            messages.success(request, 'La suppression à éffectuée avec succée!')
            return redirect('students:teacher_add_note')          
            
    return  render(request, 'resultats/noteDelete.html')
    

def emploisAdd(request):
    form = EmploisForm()
    if request.method == "POST":
        form = EmploisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enregistrement de emploi est fait avec succèes')                       
            form = EmploisForm()
        else:
            form = EmploisForm()
    emploisListe = Emplois.objects.all()
    
    return render(request, 'resultats/emploiAdd.html', {'form':form, 'emplois':emploisListe})


def EmploisUpdate(request, pk=None):

    if not pk is None:
        data = Emplois.objects.get(id=pk)
        form = EmploisForm(instance=data)
        if request.method == "POST":
            form = EmploisForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                messages.success(request, 'Enregistrement est faite avec succès')
                return redirect('students:add_emplois') 
            else:
                form = EmploisForm()
    context ={'form':form}

    return render(request, 'resultats/emploiUpdate.html', context)


def EmploisDelete(request, pk=None):
    
    if not pk is None:
        query = Emplois.objects.get(id=pk)
        if request.POST:
            query.delete()
            messages.success(request, 'La suppression à éffectuée avec succèe!')
            return redirect('students:add_emplois')          
        else:
            messages.error(request, 'Erreur de suppression!')

   
    return render(request, 'resultats/emploiDelete.html')


#fonction qui permet de filtrer tous les notes de l'étudiant qui composée
def shownote(request, id):

    if id is not None:
        etudiant = Etudiant.objects.get(id=id)
        etu_note = etudiant.note_set.all().distinct('matiere')
        context = {'etudiant':etu_note}
    else:
        context = {}

    return render(request, 'resultats/noteShow.html', context)


# ----------------Fonction de communiquer----------------------

def communiquer(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'enregistrement est faite avec succée")
            form = CommentForm()
        else:
            messages.error("l'enregistrement échoué!")
    view_comment = Comment.objects.all()
    return render(request, 'resultats/communique.html', {'form':form, 'view_comment':view_comment})


def CommentUpdate(request, pk=None):

    if not pk is None:
        data = Comment.objects.get(id=pk)
        form = CommentForm(instance=data)
        if request.method == "POST":
            form = CommentForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                messages.success(request, 'La modification est faite avec succès')
                return redirect('students:add_comment') 
            else:
                form = CommentForm()
    context ={'form':form}

    return render(request, 'resultats/commentUpdate.html', context)

def CommentDelete(request, pk=None):
    
    if not pk is None:
        query = Comment.objects.get(id=pk)
        if request.POST:
            query.delete()
            messages.success(request, 'La suppression à éffectuée avec succèe!')
            return redirect('students:add_comment')          

   
    return render(request, 'resultats/commentDelete.html')



# ----------------Fonction de generer un pdf----------------------

def generatepdf(request, id):
    liste = Etudiant.objects.get(id=id)
    template_path = "pdf_carte/generer.html"
    context = {'table':liste}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename ="page_imprimer.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("we  had some errors <pre>"+ html +"<pre>")
    return response