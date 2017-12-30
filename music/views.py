from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.urls import reverse, reverse_lazy


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

class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class AlbumUpdateView(UpdateView):
    model = Album
    template_name = "music/edit.html"
    fields = ['artist', 'title', 'genre', 'logo']
