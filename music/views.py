
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album

# Sync HTML views with models and database

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    # Default value is 'object_list'
    context_object_name = 'album_list'

    # Return all albums from database for index.html
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    # Object list name is model name by default
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    # Specify which fields the user can fill out
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    # template_name is automatically <class_name>_form.html
