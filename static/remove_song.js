function removeSong(songId) {
    const formData = new FormData();
    formData.append('songId', songId);
    fetch(`/remove_song/${playlistId}/`, {
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
