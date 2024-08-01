from django.db import models

# annexe scolaire model
class AnneeScolaire(models.Model):
    libelle = models.CharField(max_length=9)
    debut = models.DateField()
    fin = models.DateField()
    
    def __str__(self):
        return self.libelle

# grade model
class Grade(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    ordre = models.IntegerField()

    class Meta:
        ordering = ['ordre']
    
    def __str__(self):
        return self.libelle
    
# type enseignement model
class TypeEnseignement(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.libelle

# Serie model
class Serie(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    type_enseignement = models.ForeignKey(TypeEnseignement, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.libelle

# Niveau model
class Niveau(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    ordre = models.IntegerField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    serie = models.ManyToManyField(Serie, blank=True)

    class Meta:
        unique_together = ('grade', 'ordre')
        ordering = ['ordre']
    
    def __str__(self):
        return self.libelle
    
# type parent model
class TypeParent(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.libelle

# Matiere model
class Matiere(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.libelle
    
# ecole model
class Ecole(models.Model):
    nom = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    slogan = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='images/basic/ecoles/')
    
    def __str__(self):
        return f"{self.nom}"
    

# ecole model
class TypeFrais(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.libelle}"
    
# ecole model
class Frais(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.libelle}"
    
# type PAT model
class TypeEleve(models.Model):
    libelle = models.CharField(max_length=50, unique=True)
    
# type PAT model
class TypePat(models.Model):
    libelle = models.CharField(max_length=50, unique=True)