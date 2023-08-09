# Generated by Django 4.2.3 on 2023-07-29 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('descuentoEspecial', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('antiguedad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=50)),
                ('descripcionServicio', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Servicios',
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]
