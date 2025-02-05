from django.db import models

# Create your models here.




class anneeScolaire(models.Model):
    anneescolaire = models.CharField(max_length=100,blank=False, null=False)
    annee_debut = models.DateField(blank=False, null=False)
    annee_fin = models.DateField(blank=False, null=False)

    def __str__(self):
        return str(self. anneescolaire) 


class Departement(models.Model):
    nom_departement = models.CharField(max_length=100,null=False,blank=False)
    code_departement = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.code_departement)



class Filiere(models.Model): 
    nom_filiere = models.CharField(max_length=200, null=False, blank=False)
    code_filiere = models.CharField(max_length=100, null=False, blank=False)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return f'{self.code_filiere}'




 

class ClassRoom(models.Model):
    nom_classe = models.CharField(max_length=150, null=False, blank=False)
    code_classe = models.CharField(max_length=150, null=False, blank=False)
    
    def __str__(self):
        return f'{self.code_classe}'





class Specialite(models.Model):
    nom_specialite = models.CharField(max_length=200, null=True,blank=True )
    code_specialite = models.CharField(max_length=150, null=True, blank=True)
    filiere = models.ForeignKey(Filiere, on_delete = models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.code_specialite





class Semestre(models.Model):
    SELECT_SEMESTRE = (
        ('semestre1', 'semestre1'),
        ('semestre2', 'semestre2'),
        ('semestre3', 'semestre3'),
        ('semestre4', 'semestre4'),
        ('semestre5', 'semestre5'),
        ('semestre6', 'semestre6'),
    )
    SELECT_CODE = [
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4'),
        ('S5', 'S5'),
        ('S6', 'S6'),
    ]
    nom_semestre = models.CharField(max_length=100, choices=SELECT_SEMESTRE)
    code_semestre = models.CharField(max_length=150, choices=SELECT_CODE)


    def __str__(self):
        return "{}".format(self.code_semestre)



class Niveau(models.Model):
    SELECT_NIVEAU = (
        ('Licence1', 'Licence1'),
        ('Licence2', 'Licence2'),
        ('Licence3', 'Licence3'),
    )
    SELECT_CODE = (
        ('L1', 'L1'),
        ('L2', 'L2'),
        ('L3', 'L3'),
    )
    nom_niveau = models.CharField(max_length=150, null=False, choices=SELECT_NIVEAU)
    code_niveau = models.CharField(max_length=150, null=False, choices=SELECT_CODE)
    anneeScolaire = models.ForeignKey(anneeScolaire, on_delete=models.PROTECT,  null=False)


    def __str__(self):
        return f'{self.code_niveau}'
    


class Matiere(models.Model):
    nom_matiere = models.CharField(max_length=200, null=False, blank=True)
    code_matiere = models.CharField(max_length=50,null=True,blank=True)
    nature_ue = models.CharField(max_length=50,null=True,blank=True)
    code_ue = models.CharField(max_length=50,null=True,blank=True)
    coefficient_matiere = models.DecimalField(max_digits=4, decimal_places=2,help_text="s'il vous entrer un nombre qui est valide")
    horaire = models.IntegerField()
    filMatiere = models.ManyToManyField(Filiere)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, null=False)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, null=False)
    specialite = models.ManyToManyField(Specialite)
    
    

    def __str__(self):
        return f'{self.nom_matiere} / {self.code_ue}'





class Tuteur(models.Model):
    TYPE_SEXE = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]
    nom = models.CharField(max_length=150, null=True)
    prenom = models.CharField(max_length=150, null=True)
    telephone = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    adresse = models.CharField(max_length=150, null=True)
    adresse_physique = models.CharField(max_length=150, null=True)
    sexe = models.CharField(max_length=150, choices=TYPE_SEXE, null=True, blank=True)
    photo = models.ImageField(upload_to="image_tuteur/", blank=True, null=True)

    def __str__(self):
        return f'{self.nom} {self.prenom}'




class Etudiant(models.Model):
    REGIME = (
        ('normal', 'Normal'),
        ('special', 'Special'),
    )
    TYPE_SEXE = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]
    INSCRIPTION = [
        ('OUI', 'INSCRIT(E)'),
        ('NON', 'NON INSCRIT(E)'),
    ]
  
    id_etudiant = models.CharField(max_length=150, null=True, unique=True, blank=True)
    nom = models.CharField(max_length=150, null=False, blank=True)
    prenom = models.CharField(max_length=150, null=False, blank=True)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=150 ,null=False, blank=True)
    telephone = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='image_etudiant/', null=False, blank=False)
    sexe = models.CharField(max_length=150, choices=TYPE_SEXE, null=True, blank=True)
    regime = models.CharField(max_length=150, choices=REGIME, null=True, blank=True)
    anneeScolaire = models.ForeignKey(anneeScolaire, on_delete = models.CASCADE)
    tuteur = models.ForeignKey(Tuteur, on_delete = models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete = models.CASCADE, null=False, blank=True)
    specialite = models.ForeignKey(Specialite, on_delete = models.CASCADE)
    inscription = models.CharField(max_length=150, choices=INSCRIPTION, null=True, blank=True)
   
    def __str__(self):
        return f'{self.nom} {self.prenom}'


    




class Enseignant(models.Model):
    GRADE_ENSEIGNANT = [
        ('Docteur',(
            ('D', 'Missionnaire'),
            ('P', 'permanent'),
            ('V', 'Vacateur')
        )),
        ('Ingenieur', (
            ('D', 'Missionnaire'),
            ('P', 'permanent'),
            ('V', 'Vacateur')
        )),
    ]
    TYPE_SEXE = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]
    DIPLOME = [
        ('Doctorat', 'Doctorat'),
        ('Master', 'Master'),
        ('Licence', 'Licence')
    ]
    nom = models.CharField(max_length=150, null=True, blank=True)
    prenom = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField()
    telephone = models.IntegerField()
    adresse = models.CharField(max_length=150, null=True, blank=True)
    sexe = models.CharField(max_length=150, choices=TYPE_SEXE, null=True, blank=True)
    grade = models.CharField(max_length=150, choices=GRADE_ENSEIGNANT)
    diplome = models.CharField(max_length=150, choices=DIPLOME)
    photo = models.ImageField(upload_to='image_enseignant/', null=False, blank=False)
    anneeScolaire = models.ForeignKey(anneeScolaire, on_delete=models.CASCADE, null=False, blank=True)
    classe = models.ForeignKey(ClassRoom, on_delete = models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete = models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete = models.CASCADE, null=False, blank=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null=False, blank=True)
    


    def __str__(self):
        return f'{self.nom} {self.prenom}'



   


    


#class Emploi(models.Model):
    #STATUS = [
    #    ('cours', 'COURS(S)'),
    #    ('examen', 'EXAMEN(S)'),
    #    ('control', 'CONTROL(S)'),
    #]
    #date_publication = models.DateTimeField()
    #date_debut = models.DateTimeField()
    #date_fin = models.DateTimeField()
    #nom = models.CharField(max_length=150, choices=STATUS, null=True, blank=True)
    #_anneeScolaire = models.ForeignKey(anneeScolaire, on_delete=models.PROTECT, null=False, blank=True)
    #_filiere = models.Foreignkey(Filiere, on_delete = models.PROTECT)
    #_niveau = models.Foreignkey(Niveau, on_delete = models.PROTECT)
    #_matiere = models.Foreignkey(Matiere, on_delete=models.PROTECT, null=False, blank=True)
    #_classe = models.Foreignkey(ClassRoom, on_delete = models.PROTECT)
    #_semestre = models.Foreignkey(Semestre, on_delete = models.PROTECT)
   





#class Note(models.Model):
    #cc = models.FloatField(null=True, blank=True)
    #tp = models.FloatField(null=True, blank=True)
    #et1 = models.FloatField(null=True, blank=True)
    #et2 = models.FloatField(null=True, blank=True)
    #date_controle = models.DateField(date_auto_now=True)
    #_etudiant = models.Foreignkey(Etudiant, on_delete=models.PROTECT, null=True)
    #_etudiant = models.Foreignkey(Niveau, on_delete=models.PROTECT, null=True)
    #_etudiant = models.Foreignkey(Semestre, on_delete=models.PROTECT, null=True)
    #_etudiant = models.Foreignkey(Matiere, on_delete=models.PROTECT, null=True)

    #  STATUS = [
    #    ('admis', 'ADMIS(E)'),
    #    ('addette', 'ADMIS(E) AVEC DETTE'),
    #   ('re', 'REDOUBLANT(E)'),
    #    ('ex', 'EXCLU(E)'),
    #]
#class Conduite(models.Model):
    #date_absence = models.DateTimeField()
    #id_etudiant = models.ForeignKey(Student, on_delete = models.PROTECT)
    #id_matiere = models.ForeignKey(Matiere, on_delete=models.PROTECT)
    #slug = models.SlugField()