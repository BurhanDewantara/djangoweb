from django.http import HttpResponse
from .models import Album

# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    html = ''

    for album in all_albums:
        url = "/music/" + str(album.id) +"/"
        html += '<a href="'+url+'">'+album.title+'</a><br>'

    return HttpResponse(html)

def show_detail(request, album_id):
    return HttpResponse("music id = " + str(album_id))