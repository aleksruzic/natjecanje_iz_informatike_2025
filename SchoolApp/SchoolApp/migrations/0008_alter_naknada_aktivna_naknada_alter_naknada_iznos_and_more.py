# Generated by Django 5.1.2 on 2025-02-15 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0007_rename_preuzet_zahtjev_putninalog_zakljucan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naknada',
            name='aktivna_naknada',
            field=models.BooleanField(default=0.0),
        ),
        migrations.AlterField(
            model_name='naknada',
            name='iznos',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='unosputninalog',
            name='dolazak_km',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='unosputninalog',
            name='odlazak_km',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
