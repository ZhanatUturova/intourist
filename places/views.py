from django.shortcuts import render
from.models import Place

# Create your views here.
def places(request):
    place_objects = Place.objects.all() # SELECT * FROM Place
    return render(request, 'places.html', {'places': place_objects})