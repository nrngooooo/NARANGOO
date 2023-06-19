from django.shortcuts import render
from .nemelt1 import Playsongs


def playlist_view(request):
    # create a new Playsongs instance
    my_playlist = Playsongs()

    # handle user commands
    if request.method == 'POST':
        command = request.POST['command']
        if command == 'add':
            song_name = request.POST['song']
            my_playlist.add_song(song_name)
        elif command == 'remove':
            song_name = request.POST['song']
            my_playlist.remove_song(song_name)
        elif command == 'next':
            my_playlist.move_to_next_song()
            my_playlist.print_current_song()
        elif command == 'previous':
            my_playlist.move_to_previous_song()
            my_playlist.print_current_song()
        elif command == 'current':
            my_playlist.print_current_song()
        elif command == 'print':
            my_playlist.print_current_song()
        
    # get the current song and playlist
    current_song = my_playlist.current_node.data if my_playlist.current_node else None
    playlist = []
    node = my_playlist.head
    while node:
        playlist.append(node.data)
        node = node.next

    context = {
        'current_song': current_song,
        'playlist': playlist,
    }
    return render(request, 'playlist.html', context)
