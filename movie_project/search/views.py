from django.shortcuts import render
from movie.models import Movies
from django.db.models import Q
# Create your views here.

def SeracrhResult(request):
    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        print(query)
        movies=Movies.objects.all().filter(Q(name__contains=query) | Q(plot__contains=query))
        print(movies)
        return render(request,'search.html',{'query':query,'movie':movies})