# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brand'
        db.create_table('myCloset_brand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('myCloset', ['Brand'])

        # Adding model 'Apparel'
        db.create_table('myCloset_apparel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('attribute', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pictureLink', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('locationOfPurchase', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myCloset.Brand'])),
        ))
        db.send_create_signal('myCloset', ['Apparel'])

        # Adding model 'Cloth'
        db.create_table('myCloset_cloth', (
            ('apparel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['myCloset.Apparel'], unique=True, primary_key=True)),
            ('season', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('season1', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('myCloset', ['Cloth'])

        # Adding model 'Shoes'
        db.create_table('myCloset_shoes', (
            ('apparel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['myCloset.Apparel'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('myCloset', ['Shoes'])

        # Adding model 'Category'
        db.create_table('myCloset_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('permission', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('myCloset', ['Category'])

        # Adding model 'UserProfile'
        db.create_table('myCloset_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('profielPictureLink', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('myCloset', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table('myCloset_brand')

        # Deleting model 'Apparel'
        db.delete_table('myCloset_apparel')

        # Deleting model 'Cloth'
        db.delete_table('myCloset_cloth')

        # Deleting model 'Shoes'
        db.delete_table('myCloset_shoes')

        # Deleting model 'Category'
        db.delete_table('myCloset_category')

        # Deleting model 'UserProfile'
        db.delete_table('myCloset_userprofile')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myCloset.apparel': {
            'Meta': {'object_name': 'Apparel'},
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myCloset.Brand']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationOfPurchase': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pictureLink': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        },
        'myCloset.brand': {
            'Meta': {'object_name': 'Brand'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myCloset.category': {
            'Meta': {'object_name': 'Category'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'permission': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'myCloset.cloth': {
            'Meta': {'object_name': 'Cloth', '_ormbases': ['myCloset.Apparel']},
            'apparel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['myCloset.Apparel']", 'unique': 'True', 'primary_key': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'season1': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'myCloset.shoes': {
            'Meta': {'object_name': 'Shoes', '_ormbases': ['myCloset.Apparel']},
            'apparel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['myCloset.Apparel']", 'unique': 'True', 'primary_key': 'True'})
        },
        'myCloset.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profielPictureLink': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['myCloset']