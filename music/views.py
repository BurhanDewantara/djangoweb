from django.shortcuts import render, get_object_or_404

from .models import Album, Song

# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums' : all_albums,
    }
    return render(request, "music/index.html", context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render (request, "music/detail.html", {'album':album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    song_id = request.POST['song']
    context = { 'album':album } 
    try:
        selected_song = album.song_set.get(pk=song_id)
    except (KeyError, Song.DoesNotExist):
        context['error_message'] = "Song Does Not Exist"
    else:
        selected_song.is_favorite = True
        selected_song.save()

    return render (request, "music/detail.html", context )
        