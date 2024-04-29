function searchSong() {
    const searchQuery = document.getElementById('searchSong').value;
    fetch(`/search_song/?q=${searchQuery}`)
        .then(response => response.json())
        .then(data => {
            const searchResultsDiv = document.getElementById('searchResults');
            searchResultsDiv.innerHTML = '';
            data.results.forEach(song => {
                const songElement = document.createElement('div');
                songElement.textContent = `${song.title} - ${song.artist}`;
                const addButton = document.createElement('button');
                addButton.textContent = 'Add';
                addButton.onclick = function() {
                    addSongToPlaylist(song.title, song.artist);
                };
                songElement.appendChild(addButton);
                searchResultsDiv.appendChild(songElement);
            });
        })
        .catch(error => console.error('Error:', error));
}

function addSongToPlaylist(title, artist) {
    const formData = new FormData();
    formData.append('songTitle', title);
    formData.append('songArtist', artist);
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
