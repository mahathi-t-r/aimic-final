# Generated by Django 5.0.2 on 2024-04-14 06:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_music_delete_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]