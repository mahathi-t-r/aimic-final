# music/spotify_api.py

import requests
import random

SPOTIFY_SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'



SPOTIFY_CLIENT_ID = '44610704e5214488b5a442e4749fa811'
SPOTIFY_CLIENT_SECRET = '0d72c4ba050e4630a66caceacfccfcd1'

def get_spotify_access_token():
    # Implement function to obtain Spotify access token
    # For example, you can use client credentials flow
    client_id = '44610704e5214488b5a442e4749fa811'
    client_secret = '0d72c4ba050e4630a66caceacfccfcd1'
    token_url = 'https://accounts.spotify.com/api/token'
    data = {'grant_type': 'client_credentials'}
    response = requests.post(token_url, data=data, auth=(client_id, client_secret))
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return None


def search_random_song_on_spotify(access_token):
    if not access_token:
        return None

    random_offset = random.randint(0, 1000)  # Assuming 1000 is the maximum number of songs
    params = {
        'q': 'genre:tollywood',
        'type': 'track',
        'limit': 1,
        'offset': random_offset
    }
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(SPOTIFY_SEARCH_ENDPOINT, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data.get('tracks') and data['tracks'].get('items'):
            random_song = data['tracks']['items'][0]
            album_artwork = random_song['album']['images'][0]['url'] if random_song['album']['images'] else None
            return {
                'title': random_song['name'],
                'artist': random_song['artists'][0]['name'],
                'album': random_song['album']['name'],
                'release_date': random_song['album']['release_date'],
                'preview_url': random_song['preview_url'],
                'album_artwork': album_artwork,
            }
    return None