from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

def home(request):
    #return HttpResponse('<h1>Bienvenido a la página de inicio</h1>')
    #return render(request, 'home.html')
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html',{'search':searchTerm,'movies': movies })

def about(request):
    #return HttpResponse('<h1>Bienvenido a la página de About </h1>')
    return render(request, 'about.html',{'name':'About new template'})


