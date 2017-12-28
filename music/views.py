from django.views import generic
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
