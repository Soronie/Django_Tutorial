
"""
from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
"""


from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# Create your views here.
# Takes requests from users and returns a response (often a webpage).


def index(request):
    # Retrives all album objects from the database
    all_albums = Album.objects.all()
    # Holds data for template to function correctly
    context = {'all_albums': all_albums}
    # HttpResponse is built into render() function (conversion)
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song."
        })
    else:
        # Assign the value true or false on click
        if selected_song.is_favorite:
            selected_song.is_favorite = False
        else:
            selected_song.is_favorite = True
        # Update the database with the new value
        selected_song.save()
        # Re-direct the user to the same page as before
        return render(request, 'music/detail.html', {'album': album})



