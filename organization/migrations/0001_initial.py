# Generated by Django 4.2.5 on 2023-10-10 16:56

import alpha.utilities
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Full legal name of the organization', max_length=150, verbose_name='Name')),
                ('phone', models.CharField(help_text='Primary contact phone number of the organization', max_length=20, verbose_name='Contact Phone')),
                ('address_street1', models.CharField(help_text='Street Address of the organization', max_length=150, verbose_name='Address Street 1')),
                ('address_street2', models.CharField(blank=True, help_text='Street Address of the organization', max_length=150, null=True, verbose_name='Address Street 2')),
                ('address_city', models.CharField(blank=True, help_text='City Address of the organization', max_length=150, null=True, verbose_name='Address City')),
                ('address_state', models.CharField(blank=True, help_text='State Address of the organization', max_length=150, null=True, verbose_name='Address State')),
                ('address_country', models.CharField(blank=True, help_text='Country Address of the organization', max_length=150, null=True, verbose_name='Address Country')),
                ('address_zip', models.CharField(blank=True, help_text='Zip Code of the organization', max_length=150, null=True, verbose_name='Address ZIP Code')),
                ('secret_key', models.CharField(default=alpha.utilities.random_string, editable=False, max_length=50)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organization',
            },
        ),
    ]