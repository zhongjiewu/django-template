# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'RecModel.current_search_model'
        db.alter_column(u'raas_recmodel', 'current_search_model_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['raas.SearchModel'], null=True))

        # Changing field 'RecModel.current_rank_model'
        db.alter_column(u'raas_recmodel', 'current_rank_model_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['raas.RankModel'], null=True))

    def backwards(self, orm):

        # Changing field 'RecModel.current_search_model'
        db.alter_column(u'raas_recmodel', 'current_search_model_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['raas.SearchModel']))

        # Changing field 'RecModel.current_rank_model'
        db.alter_column(u'raas_recmodel', 'current_rank_model_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['raas.RankModel']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'raas.documentfile': {
            'Meta': {'object_name': 'DocumentFile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raas.DomainConfig']"}),
            'file': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'raas.domainconfig': {
            'Meta': {'object_name': 'DomainConfig'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_rec': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'raas.field': {
            'Meta': {'object_name': 'Field'},
            'column': ('django.db.models.fields.IntegerField', [], {}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raas.DomainConfig']"}),
            'ftype': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        'raas.product': {
            'Meta': {'object_name': 'Product'},
            'brand': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raas.DomainConfig']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '500'}),
            'link': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '500'}),
            'list_price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'product_group': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'title': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        'raas.rankmodel': {
            'Meta': {'object_name': 'RankModel'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raas.DomainConfig']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'raas.recmodel': {
            'Meta': {'object_name': 'RecModel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_rank_model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raas.RankModel']", 'null': 'True', 'blank': 'True'}),
            'current_search_model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raas.SearchModel']", 'null': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raas.DomainConfig']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'raas.recresults': {
            'Meta': {'object_name': 'RecResults'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raas.DomainConfig']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'source': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'target': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        'raas.searchmodel': {
            'Meta': {'object_name': 'SearchModel'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raas.DomainConfig']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['raas']