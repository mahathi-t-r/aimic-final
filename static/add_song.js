function addSong() {
    const formData = new FormData();
    formData.append('songTitle', document.getElementById('songTitle').value);
    formData.append('songArtist', document.getElementById('songArtist').value);
    formData.append('playlistId', document.getElementById('playlistId').value);
    fetch('/add_song/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
    })
    .then(response => response.json())
    .then(data => console.log(data)) // Handle success or error
    .catch(error => console.error('Error:', error));
}
