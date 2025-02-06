from django.shortcuts import render, redirect
from .models import *

def pageAccueil(request):
    student = Etudiant.objects.all()
    student_count = student.count()
   
    dawm = student.filter(filiere__code_filiere__icontains="d.a.w.m").count()
    asrs = student.filter(filiere__code_filiere__icontains="a.s.r.s").count()
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


    context = {'matiere':matiere, 'student':student, 'student_count':student_count,'dawm':dawm,"asrs":asrs, 
               'annee':annee, 'tuteur':tuteur, 'departement':departement,'filiere':filiere, 'enseignant':enseignant,
               'niveau':niveau, 'semestre':semestre, 'specialite':specialite, 'classe':classe}
    return render(request, 'roles/accueil.html', context)