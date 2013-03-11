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

        # Adding model 'ApparelType'
        db.create_table('myCloset_appareltype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('barcode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('attribute', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pictureLink', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myCloset.Brand'])),
        ))
        db.send_create_signal('myCloset', ['ApparelType'])

        # Adding model 'ApparelInstance'
        db.create_table('myCloset_apparelinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myCloset.ApparelType'])),
            ('timeOfCreation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('locationOfPurchase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myCloset.Location'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='apparels', to=orm['auth.User'])),
        ))
        db.send_create_signal('myCloset', ['ApparelInstance'])

        # Adding M2M table for field categories on 'ApparelInstance'
        db.create_table('myCloset_apparelinstance_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('apparelinstance', models.ForeignKey(orm['myCloset.apparelinstance'], null=False)),
            ('category', models.ForeignKey(orm['myCloset.category'], null=False))
        ))
        db.create_unique('myCloset_apparelinstance_categories', ['apparelinstance_id', 'category_id'])

        # Adding model 'ClothType'
        db.create_table('myCloset_clothtype', (
            ('appareltype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['myCloset.ApparelType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('myCloset', ['ClothType'])

        # Adding model 'ShoesType'
        db.create_table('myCloset_shoestype', (
            ('appareltype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['myCloset.ApparelType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('myCloset', ['ShoesType'])

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
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('profilePictureLink', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('myCloset', ['UserProfile'])

        # Adding M2M table for field friends on 'UserProfile'
        db.create_table('myCloset_userprofile_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_userprofile', models.ForeignKey(orm['myCloset.userprofile'], null=False)),
            ('to_userprofile', models.ForeignKey(orm['myCloset.userprofile'], null=False))
        ))
        db.create_unique('myCloset_userprofile_friends', ['from_userprofile_id', 'to_userprofile_id'])

        # Adding model 'Location'
        db.create_table('myCloset_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('myCloset', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table('myCloset_brand')

        # Deleting model 'ApparelType'
        db.delete_table('myCloset_appareltype')

        # Deleting model 'ApparelInstance'
        db.delete_table('myCloset_apparelinstance')

        # Removing M2M table for field categories on 'ApparelInstance'
        db.delete_table('myCloset_apparelinstance_categories')

        # Deleting model 'ClothType'
        db.delete_table('myCloset_clothtype')

        # Deleting model 'ShoesType'
        db.delete_table('myCloset_shoestype')

        # Deleting model 'Category'
        db.delete_table('myCloset_category')

        # Deleting model 'UserProfile'
        db.delete_table('myCloset_userprofile')

        # Removing M2M table for field friends on 'UserProfile'
        db.delete_table('myCloset_userprofile_friends')

        # Deleting model 'Location'
        db.delete_table('myCloset_location')


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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['myCloset.UserProfile']", 'symmetrical': 'False', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'profilePictureLink': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['myCloset']