# Generated by Django 5.0.2 on 2024-04-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_playlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
            ],
        ),
    ]
