from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
import base64
import requests
from .models import Feedback
import lyricsgenius as lg
import os
from django.http import FileResponse
from .models import Music
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import razorpay
from django.conf import settings


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                #log user in
                user_login = auth.authenticate(username=username,password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def aboutus(request):
    return render(request, 'aboutus.html')

def search(request):
    return render(request, 'search.html')

def library(request):
    return render(request, 'library.html')

def search_tracks(request):
    query = request.GET.get('q', '')
    if query:
        access_token = get_spotify_access_token()
        if access_token:
            search_results = search_tracks_on_spotify(query, access_token)
            return render(request, 'search_results.html', {'tracks': search_results})
    return render(request, 'search_form.html')

def get_spotify_access_token():
    url = 'https://accounts.spotify.com/api/token'
    client_id = '44610704e5214488b5a442e4749fa811'
    client_secret = '0d72c4ba050e4630a66caceacfccfcd1'
    headers = {'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode()}
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get('access_token')
    return None

def search_tracks_on_spotify(query, access_token):
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': 'Bearer ' + access_token}
    params = {'q': query, 'type': 'track'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        tracks_data = response.json().get('tracks', {}).get('items', [])
        tracks_info = []
        for track_data in tracks_data:
            track_info = {
                'name': track_data.get('name'),
                'artists': [artist.get('name') for artist in track_data.get('artists', [])],
                'album': track_data.get('album', {}).get('name'),
                'preview_url': track_data.get('preview_url'),
                'album_artwork': track_data.get('album', {}).get('images', [{}])[0].get('url')  # Get the first available image URL
            }
            tracks_info.append(track_info)
        return tracks_info
    return []


def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        feedback_text = request.POST['feedback_text']

        feedback_instance = Feedback.objects.create(name=name, email=email, feedback_text=feedback_text)
        messages.success(request, 'Thank you for your feedback!')
        return redirect('/')
    else:
        return render(request, 'feedback.html')


genius = lg.Genius('o2Kw8cnBKeCPUfPmjyGsTXlKmz3WjGjS3UaeZYGAkjAnQjL85Br9Utm5tv9xC4Yf')

@login_required(login_url='login')
def download_lyrics(request):
    if request.method == 'POST':
        song = request.POST.get('song')
        action = request.POST.get('action')

        if action == 'Download':
            try:
                result = genius.search_song(song)
                if result:
                    filename = f"{song}_lyrics.txt"
                    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', filename)
                    with open(desktop_path, "w", encoding="utf-8") as file:
                        file.write(result.lyrics)
                    return HttpResponse(f"Lyrics downloaded successfully! <a href='/'>Go back</a>")
                else:
                    return HttpResponse("Song not found")
            except Exception as e:
                return HttpResponse(f"Error downloading lyrics: {e}")
        elif action == 'Display':
            try:
                result = genius.search_song(song)
                if result:
                    lyrics = {song: result.lyrics}
                    return render(request, 'display_lyrics.html', {'lyrics': lyrics})
                else:
                    return HttpResponse("Song not found")
            except Exception as e:
                return HttpResponse(f"Error displaying lyrics: {e}")
    return render(request, 'download_lyrics.html')

def sid_sriram(request):
    return render(request, 'sid_sriram.html')
def taylor(request):
    return render(request, 'taylor.html')
def anirudh(request):
    return render(request,'anirudh.html')

def dsp(request):
    return render(request,'dsp.html')
def shreyagoshal(request):
    return render(request,'shreyagoshal.html')

def music_list(request):
    music_list = Music.objects.all()
    return render(request, 'music_list.html', {'music_list': music_list})

from .utils import get_spotify_access_token, search_kids_songs_on_spotify,  search_bollywood_songs_on_spotify, search_tollywood_songs_on_spotify

def kids_songs(request):
    access_token = get_spotify_access_token()
    kids_songs = search_kids_songs_on_spotify(access_token)
    return render(request, 'kids_songs.html', {'kids_songs': kids_songs})

def bollywood_songs(request):
    access_token = get_spotify_access_token()
    bollywood_songs = search_bollywood_songs_on_spotify(access_token)
    return render(request, 'bollywood_songs.html', {'bollywood_songs': bollywood_songs})

def tollywood_songs(request):
    access_token = get_spotify_access_token()
    tollywood_songs = search_tollywood_songs_on_spotify(access_token)
    return render(request, 'tollywood_songs.html', {'tollywood_songs': tollywood_songs})

from .models import Subscription

def upgrade(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        plan = request.POST.get('plan')

        # Create a new subscription object
        subscription = Subscription(name=name, email=email, phone=phone, plan=plan)
        subscription.save()

        # Redirect to a success page or do something else
        return redirect('payment')

    return render(request, 'upgrade.html')

def payment(request):
    return render(request,'payment.html')


def payment_success(request):
    return render(request, 'payment_success.html')

def payment_fail(request):
    return render(request, 'payment_fail.html')


def razor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000  # Amount in paisa

        client = razorpay.Client(auth=("rzp_test_te4SYpsbaQtEgM", "Lt736kZ5QDwx78X8rKVbEBRS"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        return render(request, 'razor.html', {'razorpay_key': "rzp_test_te4SYpsbaQtEgM", 'payment_id': payment['id']})

    return render(request, 'razor.html')





from .spotify_api import get_spotify_access_token, search_random_song_on_spotify

def random_spotify_song(request):
    access_token = get_spotify_access_token()
    random_song = search_random_song_on_spotify(access_token)
    return render(request, 'random_song.html', {'random_song': random_song})


def team(request):
    return render(request,'team.html')

def anuvjain(request):
    return render(request,'anuv.html')