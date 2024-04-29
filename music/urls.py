from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('search', views.search, name='search'),
    path('library', views.library, name='library'),
    path('search_tracks', views.search_tracks, name='search_tracks'),
    path('feedback', views.feedback, name='feedback'),
    path('download-lyrics', views.download_lyrics, name='download_lyrics'),
    path('sid_sriram', views.sid_sriram, name='sid_sriram'),
    path('taylor', views.taylor, name='taylor'),
    path('anirudh', views.anirudh, name='anirudh'),
    path('dsp', views.dsp, name='dsp'),
    path('shreyagoshal', views.shreyagoshal, name='shreyagoshal'),
    path('music', views.music_list, name='music_list'),
    path('kids', views.kids_songs, name='kids_songs'),
    path('bollywood', views.bollywood_songs, name='bollywood_songs'),
    path('tollywood', views.tollywood_songs, name='tollywood_songs'),
    path('upgrade', views.upgrade, name='upgrade'),
    path('payment', views.payment, name='payment'),
    path('paymentsuccess', views.payment_success, name='paymentsuccess'),
    path('paymentfail', views.payment_fail, name='paymentfail'),
    path('razor', views.razor, name='razor'),
    path('random', views.random_spotify_song, name='random_spotify_song'),
    path('team', views.team, name='team'),
    path('anuvjain', views.anuvjain, name='anuvjain'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
