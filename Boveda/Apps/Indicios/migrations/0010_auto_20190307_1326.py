# Generated by Django 2.1.7 on 2019-03-07 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Indicios', '0009_auto_20190307_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicio',
            old_name='userlogo',
            new_name='Imagen',
        ),
    ]