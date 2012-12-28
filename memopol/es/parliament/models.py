from django.db import models
from memopol.reps.models import Representative, Party

class ESParlamentary(Representative):
    ce_id = models.IntegerField(unique=True) # ID in congreso.es
    ce_email = models.CharField(max_length=255, null=True)
    ce_estado_civil = models.TextField(blank=True)
    ce_cargo = models.CharField(max_length=255, null=True)
    ce_cargos_anteriores = models.CharField(max_length=255, null=True)
    ce_curriculum = models.TextField(blank=True)
    ce_declaracion_bienes_url = models.URLField(default=None, null=True)
    ce_declaracion_actividades_url = models.URLField(default=None, null=True)
    ce_circunscripcion = models.CharField(max_length=255, null=True)
    ce_legislatura = models.CharField(max_length=255, null=True)
    ce_comisiones = models.TextField(blank=True)
    # party - yuhu!!
    ce_partido = models.CharField(max_length=255, null=True)
    ce_grupo_parlamentario = models.CharField(max_length=255, null=True)
    # position
    ce_pos_fila = models.IntegerField(default=None, null=True)
    ce_pos_banca = models.IntegerField(default=None, null=True)
    ce_pos_sector =  models.IntegerField(default=None, null=True)
    # social
    ce_twitter = models.URLField(default=None, null=True)
    ce_facebook_url = models.URLField(default=None, null=True)
    ce_web = models.URLField(default=None, null=True)
    ce_flickr_url = models.URLField(default=None, null=True)
    ce_linkedin_url = models.URLField(default=None, null=True)

    # personal data
#    ce_name
#    ce_lastnames

class Circunscription(models.Model):
    city = models.CharField(max_length=50)

class Party(Party):
    pass

# Legislatura
class Term(models.Model):
    current = models.BooleanField()
    begin_term = models.DateField(null=True)
    begin_reason = models.CharField(max_length=255, null=True)
    end_term = models.DateField(null=True)
    end_reason = models.CharField(max_length=255, null=True)


class Comission(models.Model):
    pass
