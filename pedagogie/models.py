from django.db import models
from django.contrib.auth.models import AbstractUser

from base_app.models import *


# user status model
class UserStatus(models.Model):
    libelle = models.CharField(max_length=50)

# base user model
class User(AbstractUser):
    profil = models.ForeignKey(UserStatus, on_delete=models.CASCADE, null=True, blank=True, default=None)

# PAT model
class Pat(User):
    role = models.ForeignKey(TypePat, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.role} - {self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "PAT"
        verbose_name_plural = "PATs"

# parent model
class Parent(User):
    role = models.ForeignKey(TypeParent, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.role} - {self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

# lv2 model
class Lv2(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.matiere)

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
    matiere = models.ManyToManyField(Matiere)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"
    
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
class SuivieEleve(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    detail = models.FloatField()
    
    def __str__(self):
        return f"suivie {self.eleve}"

# evaluation model
class Evaluation(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='eleve_evaluation')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='matiere_evaluation')
    note = models.IntegerField()
    
    def __str__(self):
        return f"{self.eleve} - {self.note} - {self.matiere}"
    
# inscription model
class Inscription(models.Model):
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