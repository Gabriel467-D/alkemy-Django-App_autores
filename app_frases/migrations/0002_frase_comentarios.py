# Generated by Django 5.2 on 2025-04-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_frases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frase',
            name='comentarios',
            field=models.TextField(blank=True, null=True),
        ),
    ]
