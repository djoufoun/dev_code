from django.urls import path
from .import views
from students import views_count as view

app_name = "students"

urlpatterns = [
    path('generate/<int:id>', views.generatepdf, name = "generate"),

    path('pageaccueil/', view.pageAccueil, name="pageaccueil"),
    path('anneescolaire', views.Anneescolaire, name="anneescolaire"),
    path('annee_update/<int:pk>/', views.anneeUpdate, name="annee_update"),
    path('annee_delete/<int:pk>/', views.anneeDelete, name="annee_delete"),

    path('search/', views.search_all, name='search'),

    
    path('departement', views.Departements, name="departement"),
    path('departementUpdate/<int:id>', views.updateDepartement, name="departementUpdate"),
    path('departementDelete/<int:id>', views.deleteDepartement, name="departementDelete"),
   
    path('addfiliere', views.addFiliere, name="addfiliere"),
    path('updatefiliere/<int:id>/', views.updateFiliere, name="updatefiliere"),
    path('deletefiliere/<int:id>/', views.deleteFiliere, name="deletefiliere"),

    path('addmatiere/', views.addMatiere, name="addmatiere"),
    path('updatematiere/<int:id>/', views.updateMatiere, name="updatematiere"),
    path('deletematiere/<int:id>/', views.deleteMatiere, name="deletematiere"),
    path('show_matiere/<int:pk>/', views.showMatiere, name="show_matiere"),

    path('addclasse/', views.addclassRoom, name="addclasse"),
    path('updateclasse/<int:id>/', views.updateclasseRoom, name="updateclasse"),
    path('deleteclasse/<int:id>/', views.deleteclasseRoom, name="deleteclasse"),

    path('specialite', views.specialite, name="specialite"),
    path('update_specialite/<int:id>/', views.updateSpecialite, name="update_specialite"),
    path('delete_specialite/<int:id>/', views.deleteSpecialite, name="delete_specialite"),

    path('niveau', views.addNiveau, name="niveau"),
    path('update_niveau/<int:id>/', views.updateNiveau, name="update_niveau"),
    path('delete_niveau/<int:id>/', views.deleteNiveau, name="delete_niveau"),

    path('semestre', views.addSemestre, name="semestre"),
    path('update_semestre/<int:id>/', views.updateSemestre, name="update_semestre"),
    path('delete_semestre/<int:id>/', views.deleteSemestre, name="delete_semestre"),

    #STUDENS
    path('student', views.addStudent, name="student"),
    path('student_update/<int:id>/', views.studentUpdate, name="student_update"),
    path('student_delete/<int:id>/', views.studentDelete, name="student_delete"),
    path('view_student/<int:pk>/', views.studentShow, name='view_student'),

    #Tuteurs
    path('tuteur', views.tuteurAdd, name="tuteur"), 
    path('tuteur_update/<int:id>/', views.tuteurUpdate, name="tuteur_update"),
    path('tuteur_delete/<int:id>/', views.tuteurDelete, name="tuteur_delete"),
    path('view_tuteur/<int:pk>/', views.tuteurShow, name='view_tuteur'),

    #Enseignants
    #path('teacher', views.indexTeacher, name="teacher"),
    path('teacherAdd', views.teacherAdd, name="teacherAdd"),
    path('teacher_update/<int:pk>/', views.teacherUpdate, name='teacher_update'),
    path('teacher_delete/<int:pk>/', views.teacherDelete, name="teacher_delete"),
    path('teacher_show/<int:pk>/', views.teacherShow, name='teacher_show'),

    #note
    path('add_note/', views.admin_add_note, name='add_note'),
    path('teacher_add_note/', views.teacher_add_note, name='teacher_add_note'),

    path('update_note/<int:pk>/', views.UpdateNote, name='update_note'),
    path('note_delete/<int:pk>/', views.NoteDelete, name="note_delete"),
    #path('show_note/<int:id>', views.shownote, name = "show_note"),

    #emplois du temps
    path('add_emplois/', views.emploisAdd, name="add_emplois"),
    path('update_emplois/<int:pk>/', views.EmploisUpdate, name="update_emplois"),
    path('delete_emplois/<int:pk>/', views.EmploisDelete, name="delete_emplois"),

    #Communiquer
    path('add_comment/', views.communiquer, name="add_comment"),
    path('update_comment/<int:pk>/', views.CommentUpdate, name="update_comment"),
    path('delete_comment/<int:pk>/', views.CommentDelete, name="delete_comment"),
 

]
   
