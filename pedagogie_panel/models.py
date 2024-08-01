from django.db import models

from base_app.models import Matiere
from parametrage.models import AnneeScolaire
from pedagogie.models import Enseignant
    
# ClasseEnseignantMatiere model
class ClasseEnseignantMatiere(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE)
    
# cour model
class Cour(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='matiere_cour')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='classe_cour')
    
    def __str__(self):
        return f"{self.matiere} - {self.classe}"