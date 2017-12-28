from django.views import generic
from django.views.generic.edit import CreateView
from .models import Album


class AlbumListView(generic.ListView):
    model = Album
    context_object_name = 'all_albums'
    template_name = "music/index.html"
     
    def get_queryset(self):
         return Album.objects.all()


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = "music/detail.html"


class AlbumCreateView(CreateView):
    model = Album
    template_name = "music/create.html"
    fields = ['artist', 'title', 'genre', 'logo']
