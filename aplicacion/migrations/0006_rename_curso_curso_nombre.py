# Generated by Django 4.2.3 on 2023-07-30 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_alter_oferta_descuentoespecial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='curso',
            new_name='nombre',
        ),
    ]
