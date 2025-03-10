# Generated by Django 5.1.2 on 2025-02-10 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0003_zahtjev_vrsta_zahtjeva'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ulaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime_osobe', models.CharField(max_length=255)),
                ('prezime_osobe', models.CharField(max_length=255)),
                ('oib_osobe', models.CharField(max_length=255)),
                ('Razlog_dolaska', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
