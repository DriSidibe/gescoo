from django.db import models

from gescoo_app.models import Budget, Evenement, User

# type PAT model
class TypePAT(User):
    name = models.CharField(max_length=50, unique=True)

# PAT model
class PAT(User):
    role = models.ForeignKey(TypePAT, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.role} - {self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "PAT"
        verbose_name_plural = "PATs"
    
# type parent model
class TypeParent(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nom

# parent model
class Parent(User):
    role = models.ForeignKey(TypeParent, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.role} - {self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"
    
# type enseignement model
class TypeEnseignement(models.Model):
    type = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.type
    
# grade model
class Grade(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.libelle

# Serie model
class Serie(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.libelle

# Niveau model
class Niveau(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    serie = models.ManyToManyField(Serie, blank=True)
    
    def __str__(self):
        return self.libelle

# Matiere model
class Matiere(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    niveau = models.ManyToManyField(Niveau, blank=True)
    serie = models.ManyToManyField(Serie, blank=True)
    
    def __str__(self):
        return self.libelle
    
    def clean(self):
        super().clean()
        print(self.niveau)
        
        # for niveau in self.niveau:
        #     if len(niveau.serie) != 0:
        #         for serie in self.serie:
        #             if serie in niveau.serie:

# Classe model
class Classe(models.Model):
    numero = models.IntegerField()
    type = models.ForeignKey(TypeEnseignement, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.niveau} {self.niveau}"

# coefficient matiere model
class CoefficientMatiere(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    coefficient = models.FloatField()
    
    def __str__(self):
        return f"coefficient : {self.coefficient}"

# lv2 model
class Lv2(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.matiere)

# annexd scolaire model
class AnneeScolaire(models.Model):
    DECOUPAGE = [('Trimestre', 'Trimestre'), ('Semestre', 'Semestre')]
    
    annee_scolaire = models.CharField(max_length=9)
    decoupage = models.CharField(choices=DECOUPAGE, max_length=50)
    
    def __str__(self):
        return self.annee_scolaire

# message model
class Message(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expediteur')
    destinataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinataire')
    objet = models.CharField(max_length=50)
    contenu = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.expediteur} - {self.destinataire}"
    
# Enseignant model
class Enseignant(User):
    CHOICES = [('Primaire', 'Primaire'), ('College', 'College'), ('Lycee', 'Lycee')]
    
    matiere = models.ManyToManyField(Matiere)
    classe = models.ManyToManyField(Classe)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"
    
# cour model
class Cour(Evenement):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='matiere_cour')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='classe_cour')
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='enseignant_cour')
    
    def __str__(self):
        return f"{self.enseignant} - {self.matiere} - {self.classe}"
    
# Eleve model
class Eleve(User):
    CHOICES = [('Affecté(e)', 'Affecté(e)'), ('Non affecté(e)', 'Non affecté(e)')]
    
    parent = models.ManyToManyField(Parent)
    status = models.CharField(choices=CHOICES, max_length=50)
    lv2 = models.ForeignKey(Lv2, on_delete=models.CASCADE, null=True, blank=True, default=None)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"
    
# dossier scolaire model
class DossierScolaire(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='eleve_dossier_scolaire')
    
    def __str__(self):
        return f"dossier {self.eleve}"
    
# suivie eleve model
class SuivieEleve(Evenement):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    detail = models.FloatField()
    
    def __str__(self):
        return f"suivie {self.eleve}"

# evaluation model
class Evaluation(Evenement):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='eleve_evaluation')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='matiere_evaluation')
    note = models.IntegerField()
    
    def __str__(self):
        return f"{self.eleve} - {self.note} - {self.matiere}"
    
# inscription model
class Inscription(Evenement):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    handicape = models.BooleanField(default=False)
    detail_handicape = models.CharField(max_length=50, null=True, blank=True)
    eps = models.BooleanField(default=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='classe_inscription')
    rabais_frais_inscription = models.IntegerField()
    rabais_frais_scolarite = models.IntegerField()
    rabais_frais_annexe = models.IntegerField()
    
    def __str__(self):
        return f"inscription {self.eleve}"

# bulletin model
class Bulletin(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='eleve')
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE, related_name='bulletin_annee_scolaire')
    numero_decoupage = models.IntegerField()
    
    def __str__(self):
        return f"bulletin {self.eleve}"
    
# ecole model
class Ecole(models.Model):
    nom = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    type_enseignement = models.ManyToManyField(TypeEnseignement)
    niveaux = models.ManyToManyField(Niveau)
    series = models.ManyToManyField(Serie)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='budget_ecole')
    
    def __str__(self):
        return f"{self.nom}"