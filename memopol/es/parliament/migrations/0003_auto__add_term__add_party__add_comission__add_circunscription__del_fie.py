# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Term'
        db.create_table('parliament_term', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('begin_term', self.gf('django.db.models.fields.DateField')(null=True)),
            ('begin_reason', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('end_term', self.gf('django.db.models.fields.DateField')(null=True)),
            ('end_reason', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('parliament', ['Term'])

        # Adding model 'Party'
        db.create_table('parliament_party', (
            ('party_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reps.Party'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('parliament', ['Party'])

        # Adding model 'Comission'
        db.create_table('parliament_comission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('parliament', ['Comission'])

        # Adding model 'Circunscription'
        db.create_table('parliament_circunscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('parliament', ['Circunscription'])

        # Deleting field 'ESParlamentary.ce_flikr_url'
        db.delete_column('parliament_esparlamentary', 'ce_flikr_url')

        # Adding field 'ESParlamentary.ce_flickr_url'
        db.add_column('parliament_esparlamentary', 'ce_flickr_url', self.gf('django.db.models.fields.URLField')(default=None, max_length=200, null=True), keep_default=False)

        # Adding unique constraint on 'ESParlamentary', fields ['ce_id']
        db.create_unique('parliament_esparlamentary', ['ce_id'])


    def backwards(self, orm):

        # Removing unique constraint on 'ESParlamentary', fields ['ce_id']
        db.delete_unique('parliament_esparlamentary', ['ce_id'])

        # Deleting model 'Term'
        db.delete_table('parliament_term')

        # Deleting model 'Party'
        db.delete_table('parliament_party')

        # Deleting model 'Comission'
        db.delete_table('parliament_comission')

        # Deleting model 'Circunscription'
        db.delete_table('parliament_circunscription')

        # Adding field 'ESParlamentary.ce_flikr_url'
        db.add_column('parliament_esparlamentary', 'ce_flikr_url', self.gf('django.db.models.fields.URLField')(default=None, max_length=200, null=True), keep_default=False)

        # Deleting field 'ESParlamentary.ce_flickr_url'
        db.delete_column('parliament_esparlamentary', 'ce_flickr_url')


    models = {
        'categories.category': {
            'Meta': {'ordering': "('tree_id', 'lft')", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alternate_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'alternate_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'meta_extra': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['categories.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'thumbnail_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'parliament.circunscription': {
            'Meta': {'object_name': 'Circunscription'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'parliament.comission': {
            'Meta': {'object_name': 'Comission'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'parliament.esparlamentary': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'ESParlamentary', '_ormbases': ['reps.Representative']},
            'ce_cargo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ce_cargos_anteriores': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ce_circunscripcion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ce_comisiones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ce_curriculum': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ce_declaracion_actividades_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'ce_declaracion_bienes_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'ce_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ce_estado_civil': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ce_facebook_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'ce_flickr_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'ce_grupo_parlamentario': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ce_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'ce_legislatura': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ce_linkedin_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'ce_partido': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'ce_pos_banca': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'ce_pos_fila': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'ce_pos_sector': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'ce_twitter': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'ce_web': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'representative_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['reps.Representative']", 'unique': 'True', 'primary_key': 'True'})
        },
        'parliament.party': {
            'Meta': {'object_name': 'Party', '_ormbases': ['reps.Party']},
            'party_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['reps.Party']", 'unique': 'True', 'primary_key': 'True'})
        },
        'parliament.term': {
            'Meta': {'object_name': 'Term'},
            'begin_reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'begin_term': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'end_term': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'reps.opinion': {
            'Meta': {'object_name': 'Opinion'},
            '_author': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['reps.Representative']", 'null': 'True'}),
            '_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1023'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400'})
        },
        'reps.opinionrep': {
            'Meta': {'object_name': 'OpinionREP'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opinion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reps.Opinion']"}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reps.Representative']"})
        },
        'reps.party': {
            'Meta': {'object_name': 'Party'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'reps.partyrepresentative': {
            'Meta': {'object_name': 'PartyRepresentative'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reps.Party']"}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reps.Representative']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'reps.representative': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Representative'},
            'achievements': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['categories.Category']", 'symmetrical': 'False'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'birth_place': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'local_party': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reps.Party']", 'through': "orm['reps.PartyRepresentative']", 'symmetrical': 'False'}),
            'opinions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reps.Opinion']", 'through': "orm['reps.OpinionREP']", 'symmetrical': 'False'}),
            'picture': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['parliament']
