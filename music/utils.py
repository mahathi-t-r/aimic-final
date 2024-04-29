# utils.py

import base64
import requests

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

def search_kids_songs_on_spotify(access_token):
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': 'Bearer ' + access_token}
    query = 'genre:"children"'
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

def search_bollywood_songs_on_spotify(access_token):
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': 'Bearer ' + access_token}
    query = 'genre:"bollywood"'
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

def search_tollywood_songs_on_spotify(access_token):
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': 'Bearer ' + access_token}
    query = 'genre:"tollywood"'
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