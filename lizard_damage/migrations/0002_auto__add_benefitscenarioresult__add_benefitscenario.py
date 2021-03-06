# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BenefitScenarioResult'
        db.create_table('lizard_damage_benefitscenarioresult', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('benefit_scenario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lizard_damage.BenefitScenario'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('north', self.gf('django.db.models.fields.FloatField')()),
            ('south', self.gf('django.db.models.fields.FloatField')()),
            ('east', self.gf('django.db.models.fields.FloatField')()),
            ('west', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('lizard_damage', ['BenefitScenarioResult'])

        # Adding model 'BenefitScenario'
        db.create_table('lizard_damage_benefitscenario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('zip_risk_a', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('zip_risk_b', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('zip_result', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('lizard_damage', ['BenefitScenario'])


    def backwards(self, orm):
        
        # Deleting model 'BenefitScenarioResult'
        db.delete_table('lizard_damage_benefitscenarioresult')

        # Deleting model 'BenefitScenario'
        db.delete_table('lizard_damage_benefitscenario')


    models = {
        'lizard_damage.ahnindex': {
            'Meta': {'object_name': 'AhnIndex', 'db_table': "u'data_index'"},
            'ar': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bladnr': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'cellsize': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'datum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lo_x': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'lo_y': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'max_datum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'min_datum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'the_geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '28992', 'null': 'True', 'blank': 'True'}),
            'update': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_damage.benefitscenario': {
            'Meta': {'object_name': 'BenefitScenario'},
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zip_result': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zip_risk_a': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'zip_risk_b': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'lizard_damage.benefitscenarioresult': {
            'Meta': {'object_name': 'BenefitScenarioResult'},
            'benefit_scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_damage.BenefitScenario']"}),
            'east': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'north': ('django.db.models.fields.FloatField', [], {}),
            'south': ('django.db.models.fields.FloatField', [], {}),
            'west': ('django.db.models.fields.FloatField', [], {})
        },
        'lizard_damage.damageevent': {
            'Meta': {'object_name': 'DamageEvent'},
            'floodmonth': ('django.db.models.fields.IntegerField', [], {'default': '9'}),
            'floodtime': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'repairtime_buildings': ('django.db.models.fields.FloatField', [], {'default': '432000'}),
            'repairtime_roads': ('django.db.models.fields.FloatField', [], {'default': '432000'}),
            'repetition_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_damage.DamageScenario']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'table': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_damage.damageeventresult': {
            'Meta': {'object_name': 'DamageEventResult'},
            'damage_event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_damage.DamageEvent']"}),
            'east': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'north': ('django.db.models.fields.FloatField', [], {}),
            'south': ('django.db.models.fields.FloatField', [], {}),
            'west': ('django.db.models.fields.FloatField', [], {})
        },
        'lizard_damage.damageeventwaterlevel': {
            'Meta': {'ordering': "(u'index',)", 'object_name': 'DamageEventWaterlevel'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_damage.DamageEvent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'waterlevel': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'lizard_damage.damagescenario': {
            'Meta': {'object_name': 'DamageScenario'},
            'calc_type': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'damagetable': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'scenario_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'lizard_damage.roads': {
            'Meta': {'object_name': 'Roads', 'db_table': "u'data_roads'"},
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'gridcode': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'the_geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '28992', 'null': 'True', 'blank': 'True'}),
            'typeinfr_1': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'typeweg': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        },
        'lizard_damage.unit': {
            'Meta': {'object_name': 'Unit'},
            'factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lizard_damage']
