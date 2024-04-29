from django.db import models
from django.utils import timezone

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Register"

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Feedback"


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    song_file = models.FileField(upload_to='music/')
    image = models.ImageField(upload_to='images/')
    mp3_file = models.FileField(upload_to='mp3/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Music"

class Subscription(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic Plan'),
        ('premium', 'Premium Plan'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    playlists = models.ManyToManyField(Playlist, related_name='songs')

    def __str__(self):
        return f"{self.name} - {self.artist}"