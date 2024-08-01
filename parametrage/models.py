from django.db import models

from base_app.models import AnneeScolaire, Matiere, Niveau, Serie, TypeEleve, TypeEnseignement, TypeFrais

  
# annexe scolaire model
class Decoupage(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    type_enseignement = models.ForeignKey(TypeEnseignement, on_delete=models.CASCADE)
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE)
    coefficient = models.DecimalField(decimal_places=2, max_digits=3)
    debut = models.DateField()
    fin = models.DateField()
    
    def __str__(self):
        return self.libelle
    

# MatiereNiveauSerie model
class MatiereNiveauSerie(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    coefficient = models.FloatField()
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE)

# Classe model
class Classe(models.Model):
    numero = models.IntegerField()
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.niveau} {self.serie} {self.numero}"
    
# frais inscription model
class Frais(models.Model):
    type_frais = models.ForeignKey(TypeFrais, on_delete=models.CASCADE)
    montant = models.IntegerField()
    
    def __str__(self):
        return f"frais {self.pk}"
    
# frais inscription model
class FraisNiveauxSeries(models.Model):
    frais = models.ForeignKey(Frais, on_delete=models.CASCADE)
    annee_scolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    type_eleve = models.ForeignKey(TypeEleve, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"frais {self.pk}"

# frais annexe model
class FraisAnnexe(models.Model):
    niveau = models.ManyToManyField(Niveau)
    serie = models.ManyToManyField(Serie)
    montaint = models.IntegerField()
    
    def __str__(self):
        return f"frais {self.pk}"