from django.db import models
from django.contrib.auth.models import AbstractUser

# user status model
class UserStatus(models.Model):
    name = models.CharField(max_length=50)

# base user model
class User(AbstractUser):
    profil = models.ForeignKey(UserStatus, on_delete=models.CASCADE, null=True, blank=True, default=None)

# evenement model
class Evenement(models.Model):
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField(null=True, blank=True, default=None)
    
# budget model
class Budget(models.Model):
    budget = models.IntegerField()
    
    def __str__(self) -> str:
        return f"budget {self.pk}"