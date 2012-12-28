# -*- coding: utf-8 -*-
from django.contrib import admin
from memopol.es.parliament import models

class ESParlamentaryAdmin(admin.ModelAdmin):
    model = models.ESParlamentary
    list_display = ('last_name', 'first_name')

class Circunscription(admin.ModelAdmin):
    model = models.Circunscription

class Party(admin.ModelAdmin):
    model = models.Party

class Term(admin.ModelAdmin):
    model = models.Term

class Comission(admin.ModelAdmin):
    model = models.Comission

admin.site.register(models.ESParlamentary, ESParlamentaryAdmin)
admin.site.register(models.Circunscritcion, Circunscription)
admin.site.register(models.Party, Party)
admin.site.register(models.Comission, Comission)
