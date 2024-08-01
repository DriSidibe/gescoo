from django.db import models

from parametrage.models import Grade
from pedagogie.models import Classe
from pedagogie_panel.models import Matiere


# TypeEvenement model
class TypeEvenement(models.Model):
    libelle = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.libelle
    
# CrenoHoraire model
class CreneauHoraire(models.Model):
    heure_debut = models.DateTimeField()
    heure_fin = models.DateTimeField(null=True, blank=True, default=None)
    
    def __str__(self) -> str:
        return self.pk

# evenement model
class Evenement(models.Model):
    type_evenement = models.ForeignKey(TypeEvenement, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.type_evenement} {self.matiere}"
    
# EmploiDuTemp model
class EmploiDuTemp(models.Model):
    JOURS = [(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'), (7, 'Dimanche')]
    
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    creneau_horaire = models.ForeignKey(CreneauHoraire, on_delete=models.CASCADE)
    jour = models.CharField(choices=JOURS, max_length=50)
    
    def __str__(self) -> str:
        return f"{self.evenement} {self.classe}"
    
# budget model
class Budget(models.Model):
    budget = models.IntegerField()
    
    def __str__(self) -> str:
        return f"budget {self.pk}"