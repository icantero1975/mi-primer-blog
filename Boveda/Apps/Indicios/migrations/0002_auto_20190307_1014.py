# Generated by Django 2.1.7 on 2019-03-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicio',
            name='Cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='indicio',
            name='Deposita_Banco',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], default='S', max_length=1),
        ),
    ]
