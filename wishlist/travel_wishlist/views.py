from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.


def place_list(request):
    if request.method == 'POST':
        #creating new form
        form = NewPlaceForm(request.POST)
        place = form.save() # creating a new model object from here
        if form.is_valid(): # validation
            place.save()
            return redirect('place_list') # reloads home page
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited })


def place_was_visited(request, place_pk):
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()
    # return redirect('places_visited')
    return redirect('place_list')



def about(request):
    author = 'Khadar'
    about = 'A website to create a list of place to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about })


