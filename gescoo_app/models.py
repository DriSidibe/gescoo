from django.db import models
from django.contrib.auth.models import AbstractUser

class UserStatus(models.Model):
    name = models.CharField(max_length=50)

# app base user model
class User(AbstractUser):
    profil = models.ForeignKey(UserStatus, on_delete=models.CASCADE)

# parent model
class Parent(User):
    CHOICES = [('Pere', 'Pere'), ('Mere', 'Mere'), ('Tuteur', 'Tuteur')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_user', parent_link=True)
    role = models.CharField(choices=CHOICES, max_length=50)
    
class Evenement(models.Model):
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField(null=True, blank=True, default=None)
    
# Niveau model
class Niveau(models.Model):
    nom = models.CharField(max_length=50)

# Serie model
class Serie(models.Model):
    nom = models.CharField(max_length=50)
    
# Matiere model
class Matiere(models.Model):
    nom = models.CharField(max_length=50)
    niveau = models.ManyToManyField(Niveau)
    serie = models.ManyToManyField(Serie)
    
class TypeEnseignement(models.Model):
    type = models.CharField(max_length=50)
    
# Classe model
class Classe(models.Model):
    numero = models.IntegerField()
    type = models.ForeignKey(TypeEnseignement, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    
# Enseignant model
class Enseignant(User):
    CHOICES = [('Primaire', 'Primaire'), ('College', 'College'), ('Lycee', 'Lycee')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='enseignant_user', parent_link=True)
    matiere = models.ManyToManyField(Matiere)
    classe = models.ManyToManyField(Classe)
    grade = models.CharField(max_length=50, choices=CHOICES)
    
class FraisInscription(models.Model):
    montaint = models.IntegerField()
    niveau = models.ManyToManyField(Niveau)
    serie = models.ManyToManyField(Serie)
    
class FraisScolarite(models.Model):
    niveau = models.ManyToManyField(Niveau)
    serie = models.ManyToManyField(Serie)
    montaint = models.IntegerField()
    
class FraisAnnexe(models.Model):
    niveau = models.ManyToManyField(Niveau)
    serie = models.ManyToManyField(Serie)
    montaint = models.IntegerField()
    
class coefficientMatiere(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    coefficient = models.FloatField()
    
class Lv2(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    
# Eleve model
class Eleve(User):
    CHOICES = [('Affecté(e)', 'Affecté(e)'), ('Non affecté(e)', 'Non affecté(e)')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='eleve_user', parent_link=True)
    parent = models.ManyToManyField(Parent)
    status = models.CharField(choices=CHOICES, max_length=50)
    lv2 = models.ForeignKey(Lv2, on_delete=models.CASCADE, null=True, blank=True, default=None)
    
class SuivieEleve(Evenement):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    detail = models.FloatField()
    
# PAT model
class PAT(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pat_user', parent_link=True)
    
# contrat model
class Contrat(Evenement):
    CHOICES = [('CDD', 'CDD'), ('CDI', 'CDI'), ('Vacataire', 'Vacataire'), ('Stagiaire', 'Stagiaire'), ('Contractuel', 'Contractuel'), ('Autre', 'Autre')]
    
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, null=True, blank=True, default=None)
    pat = models.ForeignKey(PAT, on_delete=models.CASCADE, null=True, blank=True, default=None)
    type_contrat = models.CharField(max_length=50, choices=CHOICES)
    salaire = models.IntegerField()
    
class Paiement(Evenement):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    pat = models.ForeignKey(PAT, on_delete=models.CASCADE)

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
    
class TypePaiement(models.Model):
    type = models.CharField(max_length=50)
    
class Versement(Evenement):
    type = models.ForeignKey(TypePaiement, on_delete=models.CASCADE, related_name='type_versement')
    inscription_versement = models.ForeignKey(Inscription, on_delete=models.CASCADE, related_name='inscription_versement')
    montant_restant = models.IntegerField()
    
class Budget(models.Model):
    budget = models.IntegerField()
    
class Ecole(models.Model):
    nom = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    type_enseignement = models.ManyToManyField(TypeEnseignement)
    niveaux = models.ManyToManyField(Niveau)
    series = models.ManyToManyField(Serie)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='budget_ecole')
    
class Depense(Evenement):
    montant = models.IntegerField()
    raison = models.TextField()
    
class DossierScolaire(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='eleve_dossier_scolaire')
    
class Cour(Evenement):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='matiere_cour')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='classe_cour')
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='enseignant_cour')
    
class Evaluation(Evenement):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='eleve_evaluation')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='matiere_evaluation')
    note = models.IntegerField()
    
class AnneeScolaire(models.Model):
    DECOUPAGE = [('Trimestre', 'Trimestre'), ('Semestre', 'Semestre')]
    
    annee_scolaire = models.CharField(max_length=9)
    decoupage = models.CharField(choices=DECOUPAGE, max_length=50)
    
class Bulletin(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='eleve')
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE, related_name='bulletin_annee_scolaire')
    numero_decoupage = models.IntegerField()
    
class Message(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expediteur')
    destinataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinataire')
    objet = models.CharField(max_length=50)
    contenu = models.TextField()
    date = models.DateTimeField()