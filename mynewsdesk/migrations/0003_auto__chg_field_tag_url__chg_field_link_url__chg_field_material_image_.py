# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tag.url'
        db.alter_column('mynewsdesk_tag', 'url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Link.url'
        db.alter_column('mynewsdesk_link', 'url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.image_thumbnail_small'
        db.alter_column('mynewsdesk_material', 'image_thumbnail_small', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.image'
        db.alter_column('mynewsdesk_material', 'image', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.flash_video'
        db.alter_column('mynewsdesk_material', 'flash_video', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.image_thumbnail_large'
        db.alter_column('mynewsdesk_material', 'image_thumbnail_large', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.signup_url'
        db.alter_column('mynewsdesk_material', 'signup_url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.download_url'
        db.alter_column('mynewsdesk_material', 'download_url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.document'
        db.alter_column('mynewsdesk_material', 'document', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.thumbnail'
        db.alter_column('mynewsdesk_material', 'thumbnail', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.image_thumbnail_medium'
        db.alter_column('mynewsdesk_material', 'image_thumbnail_medium', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.attached_doc'
        db.alter_column('mynewsdesk_material', 'attached_doc', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.url'
        db.alter_column('mynewsdesk_material', 'url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

        # Changing field 'Material.attached_pdf'
        db.alter_column('mynewsdesk_material', 'attached_pdf', self.gf('django.db.models.fields.URLField')(max_length=500, null=True))

    def backwards(self, orm):

        # Changing field 'Tag.url'
        db.alter_column('mynewsdesk_tag', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Link.url'
        db.alter_column('mynewsdesk_link', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.image_thumbnail_small'
        db.alter_column('mynewsdesk_material', 'image_thumbnail_small', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.image'
        db.alter_column('mynewsdesk_material', 'image', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.flash_video'
        db.alter_column('mynewsdesk_material', 'flash_video', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.image_thumbnail_large'
        db.alter_column('mynewsdesk_material', 'image_thumbnail_large', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.signup_url'
        db.alter_column('mynewsdesk_material', 'signup_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.download_url'
        db.alter_column('mynewsdesk_material', 'download_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.document'
        db.alter_column('mynewsdesk_material', 'document', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.thumbnail'
        db.alter_column('mynewsdesk_material', 'thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.image_thumbnail_medium'
        db.alter_column('mynewsdesk_material', 'image_thumbnail_medium', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.attached_doc'
        db.alter_column('mynewsdesk_material', 'attached_doc', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.url'
        db.alter_column('mynewsdesk_material', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Material.attached_pdf'
        db.alter_column('mynewsdesk_material', 'attached_pdf', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    models = {
        'mynewsdesk.channel': {
            'Meta': {'object_name': 'Channel'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mynewsdesk.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'mynewsdesk.link': {
            'Meta': {'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': "orm['mynewsdesk.Material']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'mynewsdesk.material': {
            'Meta': {'object_name': 'Material'},
            'attached_doc': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'attached_pdf': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'boilerplate': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'channels': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'materials'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['mynewsdesk.Channel']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'document': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'document_format': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'document_size': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'embed_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event_types': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'materials'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['mynewsdesk.EventType']"}),
            'flash_video': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'flash_video_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flash_video_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'image_dimensions': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'image_format': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'image_size': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image_thumbnail_large': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'image_thumbnail_medium': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'image_thumbnail_small': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'organization_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'phone_alternative': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'photographer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pressroom': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'pressroom_contact': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'pressroom_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pressroom_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {}),
            'signup_url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'source_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'source_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'specialist': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'materials'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['mynewsdesk.Tag']"}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type_of_media': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'mynewsdesk.tag': {
            'Meta': {'object_name': 'Tag'},
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mynewsdesk']