# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('mynewsdesk_tag')

        # Deleting model 'Link'
        db.delete_table('mynewsdesk_link')

        # Deleting model 'Channel'
        db.delete_table('mynewsdesk_channel')

        # Deleting model 'EventType'
        db.delete_table('mynewsdesk_eventtype')

        # Deleting model 'Material'
        db.delete_table('mynewsdesk_material')

        # Removing M2M table for field channels on 'Material'
        db.delete_table(db.shorten_name('mynewsdesk_material_channels'))

        # Removing M2M table for field event_types on 'Material'
        db.delete_table(db.shorten_name('mynewsdesk_material_event_types'))

        # Removing M2M table for field tags on 'Material'
        db.delete_table(db.shorten_name('mynewsdesk_material_tags'))


    def backwards(self, orm):
        # Adding model 'Tag'
        db.create_table('mynewsdesk_tag', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('mynewsdesk', ['Tag'])

        # Adding model 'Link'
        db.create_table('mynewsdesk_link', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(related_name='links', to=orm['mynewsdesk.Material'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('mynewsdesk', ['Link'])

        # Adding model 'Channel'
        db.create_table('mynewsdesk_channel', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('mynewsdesk', ['Channel'])

        # Adding model 'EventType'
        db.create_table('mynewsdesk_eventtype', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('mynewsdesk', ['EventType'])

        # Adding model 'Material'
        db.create_table('mynewsdesk_material', (
            ('image_thumbnail_small', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('source_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('header', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_format', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('signup_url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('embed_code', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pressroom', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('download_url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pressroom_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('boilerplate', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pressroom_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image_dimensions', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('image_size', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('organization_number', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('attached_pdf', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('pressroom_contact', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('flash_video_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('image_thumbnail_large', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('document_format', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('end_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('document', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('specialist', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('document_size', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('type_of_media', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('image_thumbnail_medium', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('attached_doc', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
            ('flash_video_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('phone_alternative', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('photographer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('source_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('flash_video', self.gf('django.db.models.fields.URLField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('mynewsdesk', ['Material'])

        # Adding M2M table for field channels on 'Material'
        m2m_table_name = db.shorten_name('mynewsdesk_material_channels')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('material', models.ForeignKey(orm['mynewsdesk.material'], null=False)),
            ('channel', models.ForeignKey(orm['mynewsdesk.channel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['material_id', 'channel_id'])

        # Adding M2M table for field event_types on 'Material'
        m2m_table_name = db.shorten_name('mynewsdesk_material_event_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('material', models.ForeignKey(orm['mynewsdesk.material'], null=False)),
            ('eventtype', models.ForeignKey(orm['mynewsdesk.eventtype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['material_id', 'eventtype_id'])

        # Adding M2M table for field tags on 'Material'
        m2m_table_name = db.shorten_name('mynewsdesk_material_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('material', models.ForeignKey(orm['mynewsdesk.material'], null=False)),
            ('tag', models.ForeignKey(orm['mynewsdesk.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['material_id', 'tag_id'])


    models = {
        
    }

    complete_apps = ['mynewsdesk']