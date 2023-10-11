# Generated by Django 4.2.5 on 2023-10-11 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('client', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermeta',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='organization.organization'),
        ),
    ]
