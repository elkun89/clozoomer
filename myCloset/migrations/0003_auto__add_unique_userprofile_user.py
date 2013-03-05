# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field friends on 'UserProfile'
        db.create_table('myCloset_userprofile_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_userprofile', models.ForeignKey(orm['myCloset.userprofile'], null=False)),
            ('to_userprofile', models.ForeignKey(orm['myCloset.userprofile'], null=False))
        ))
        db.create_unique('myCloset_userprofile_friends', ['from_userprofile_id', 'to_userprofile_id'])

        # Adding unique constraint on 'UserProfile', fields ['user']
        db.create_unique('myCloset_userprofile', ['user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserProfile', fields ['user']
        db.delete_unique('myCloset_userprofile', ['user_id'])

        # Removing M2M table for field friends on 'UserProfile'
        db.delete_table('myCloset_userprofile_friends')


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
        'myCloset.apparelinstance': {
            'Meta': {'object_name': 'ApparelInstance'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['myCloset.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationOfPurchase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myCloset.Location']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apparels'", 'to': "orm['auth.User']"}),
            'timeOfCreation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myCloset.ApparelType']"})
        },
        'myCloset.appareltype': {
            'Meta': {'object_name': 'ApparelType'},
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'barcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myCloset.Brand']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        'myCloset.clothtype': {
            'Meta': {'object_name': 'ClothType', '_ormbases': ['myCloset.ApparelType']},
            'appareltype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['myCloset.ApparelType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'myCloset.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'myCloset.shoestype': {
            'Meta': {'object_name': 'ShoesType', '_ormbases': ['myCloset.ApparelType']},
            'appareltype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['myCloset.ApparelType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'myCloset.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['myCloset.UserProfile']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profielPictureLink': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['myCloset']