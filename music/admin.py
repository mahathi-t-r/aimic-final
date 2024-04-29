from django.contrib import admin
from .models import Register, Feedback, Music, Subscription
@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback_text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'feedback_text')

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'artist')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'plan', 'timestamp')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('plan', 'timestamp')


from .models import Playlist

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'user']