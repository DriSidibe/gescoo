from django.contrib import admin

from .models import *
import comptabilite.models as comptabilite_models
import pedagogie.models as pedagogie_models
import administration.models as administration_models

# Register your models here.
admin.site.register(UserStatus)
admin.site.register(User)
admin.site.register(pedagogie_models.TypeParent)
admin.site.register(pedagogie_models.Parent)
admin.site.register(Evenement)
admin.site.register(pedagogie_models.Niveau)
admin.site.register(pedagogie_models.Serie)
admin.site.register(pedagogie_models.Matiere)
admin.site.register(pedagogie_models.TypeEnseignement)
admin.site.register(pedagogie_models.Classe)
admin.site.register(pedagogie_models.Grade)
admin.site.register(pedagogie_models.Enseignant)
admin.site.register(comptabilite_models.FraisInscription)
admin.site.register(comptabilite_models.FraisScolarite)
admin.site.register(comptabilite_models.FraisAnnexe)
# admin.site.register(pedagogie_models.CoefficientMatiere)
admin.site.register(pedagogie_models.Lv2)
admin.site.register(pedagogie_models.Eleve)
admin.site.register(pedagogie_models.SuivieEleve)
admin.site.register(pedagogie_models.Pat)
admin.site.register(comptabilite_models.Contrat)
admin.site.register(comptabilite_models.Paiement)
admin.site.register(comptabilite_models.Inscription)
admin.site.register(comptabilite_models.TypePaiement)
admin.site.register(comptabilite_models.Versement)
admin.site.register(Budget)
admin.site.register(pedagogie_models.Ecole)
admin.site.register(comptabilite_models.Depense)
admin.site.register(pedagogie_models.DossierScolaire)
admin.site.register(pedagogie_models.Cour)
admin.site.register(pedagogie_models.Evaluation)
admin.site.register(pedagogie_models.AnneeScolaire)
admin.site.register(pedagogie_models.Bulletin)
admin.site.register(pedagogie_models.Message)