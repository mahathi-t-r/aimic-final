# Generated by Django 5.0.2 on 2024-04-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_music_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('plan', models.CharField(choices=[('basic', 'Basic Plan'), ('premium', 'Premium Plan')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]