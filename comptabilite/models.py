from django.db import models

from gescoo_app.models import Evenement
from pedagogie.models import Enseignant, Inscription, Niveau, Serie, PAT

# frais inscription model
class FraisInscription(models.Model):
    montant = models.IntegerField()
    niveau = models.ManyToManyField(Niveau)
    serie = models.ManyToManyField(Serie)
    
    def __str__(self):
        return f"frais {self.pk}"

# frais scolarite model
class FraisScolarite(models.Model):
    niveau = models.ManyToManyField(Niveau)
    serie = models.ManyToManyField(Serie)
    montaint = models.IntegerField()
    
    def __str__(self):
        return f"frais {self.pk}"

# frais annexe model
class FraisAnnexe(models.Model):
    niveau = models.ManyToManyField(Niveau)
    serie = models.ManyToManyField(Serie)
    montaint = models.IntegerField()
    
    def __str__(self):
        return f"frais {self.pk}"
    
# type paiement model
class TypePaiement(models.Model):
    type = models.CharField(max_length=50)
    
    def __str__(self):
        return f"frais {self.type}"

# versement model
class Versement(Evenement):
    type = models.ForeignKey(TypePaiement, on_delete=models.CASCADE, related_name='type_versement')
    inscription_versement = models.ForeignKey(Inscription, on_delete=models.CASCADE, related_name='inscription_versement')
    montant_restant = models.IntegerField()
    
    def __str__(self):
        return f"frais {self.type}"
    
# contrat model
class Contrat(Evenement):
    CHOICES = [('CDD', 'CDD'), ('CDI', 'CDI'), ('Vacataire', 'Vacataire'), ('Stagiaire', 'Stagiaire'), ('Contractuel', 'Contractuel'), ('Autre', 'Autre')]
    
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, null=True, blank=True, default=None)
    pat = models.ForeignKey(PAT, on_delete=models.CASCADE, null=True, blank=True, default=None)
    type_contrat = models.CharField(max_length=50, choices=CHOICES)
    salaire = models.IntegerField()
    
    def __str__(self):
        return f"frais {self.pk}"
    
# depense model
class Depense(Evenement):
    montant = models.IntegerField()
    raison = models.TextField()
    
    def __str__(self):
        return f"frais {self.pk}"
    
# paiement model
class Paiement(Evenement):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    pat = models.ForeignKey(PAT, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"frais {self.pk}"