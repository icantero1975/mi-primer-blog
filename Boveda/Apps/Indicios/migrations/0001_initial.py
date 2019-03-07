# Generated by Django 2.1.7 on 2019-03-07 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Expediente', models.CharField(help_text='Ingrese el Numero de Carpeta', max_length=100)),
                ('Fecha', models.DateTimeField(auto_now_add=True)),
                ('Hora', models.DateTimeField(auto_now_add=True)),
                ('Oficio', models.CharField(max_length=15)),
                ('No_Indicio', models.CharField(help_text='Ingrese el numero de indicio', max_length=10)),
                ('Tipo', models.CharField(choices=[('F', 'Fisico'), ('O', 'Organico'), ('B', 'Biologico')], default='F', max_length=1)),
                ('Descripcion', models.TextField(help_text='Describe el indicio como la etiqueta', max_length=500)),
                ('Rue', models.CharField(help_text='Format = OM/F/100/2019', max_length=15)),
                ('Clasificacion', models.CharField(choices=[('A', 'Arma de Fuego'), ('B', 'Arma Blanca'), ('D', 'Droga'), ('P', 'Perecedero'), ('E', 'Electronico'), ('AP', 'Autopartes'), ('H', 'Herramientas'), ('AB', ' Articulos de Belleza'), ('R', ' Ropa'), ('N', ' Numerario')], default='A', max_length=1)),
                ('Cadena', models.CharField(choices=[('S', 'Si'), ('N', 'No'), ('C', 'Copia')], default='S', max_length=1)),
                ('Embalaje', models.CharField(choices=[('B', 'Bolsa de Plastico'), ('BP', 'Bolsa de Papel'), ('SB', 'Sobre Blanco'), ('SM', 'Sobre Manila'), ('O', 'Otro')], default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Mp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(help_text='Nombre Completo empezando por Nombre, Apellido Paterno, Apellido Materno', max_length=50)),
                ('Cargo', models.CharField(help_text='Ingrese el cargo de la Autoridad', max_length=50)),
                ('Adscripcion', models.CharField(help_text='Ingrese el lugar de Agencia o Unidad', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='indicio',
            name='Entrega',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Indicios.Mp'),
        ),
    ]