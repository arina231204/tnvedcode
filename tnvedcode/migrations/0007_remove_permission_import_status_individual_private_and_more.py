# Generated by Django 5.0.1 on 2024-01-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnvedcode', '0006_permission_import_status_individual_private_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='import_status_individual_private',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='import_status_legal_private',
        ),
        migrations.AddField(
            model_name='tnvedcode',
            name='import_status_individual_private',
            field=models.CharField(choices=[('+', '+'), ('-', '-'), ('x', 'x')], default='-', max_length=1, verbose_name='Статус ввоза для физических лиц частных компаний'),
        ),
        migrations.AddField(
            model_name='tnvedcode',
            name='import_status_legal_private',
            field=models.CharField(choices=[('+', '+'), ('-', '-'), ('x', 'x')], default='-', max_length=1, verbose_name='Статус ввоза для юридических лиц частных компаний'),
        ),
    ]
