from django.shortcuts import render, redirect,get_object_or_404
from .models import Movies,Actors,Review,Genre
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .forms import UserAddForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def MovieList(request):
    # m_count=None
    movie_list=Movies.objects.all()
    review_list=Review.objects.all()
    genre=Genre.objects.all()
    paginator=Paginator(movie_list,10)
    # movie_list.actors.set(Actors.objects.all())
    # temp=movie_list.actors.all()
    # print(temp)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'movies':movies,'review':review_list,'genre':genre})

    # return HttpResponse("Any kind of HTML Here")



def MovieDetails(request,movie_slug):

    try:
        movie=Movies.objects.get(slug=movie_slug)
    except Exception as e:
        raise e
    if request.method=='POST':
        review=request.POST['review']
        rateing=request.POST['rateing']
        movie_name=request.POST['movie_name']
        print(review)
        us1=Review.objects.create(rating=rateing, movie=movie,review=review)
    return render (request,'movie-details.html',{'Movies':movie})

@login_required
def MovieCreate(request):
    # Do something with the movie
    print(request.method)
    if request.method == 'POST':
        form = UserAddForm(request.POST or None,request.FILES,user=request.user)
        print(form.is_valid())
        if form.is_valid():
            # movie = form.save(commit=False)
            # movie.added_by = request.user  # Assign the current user to the added_by field
            form.save()
            return redirect('/')
    else:
        print("this is not worked")
        form=UserAddForm()
    return render(request,'add_movie.html',{'form': form})
@login_required
def MovieEdit(request,movie_id):
    print(movie_id)
    movie = get_object_or_404(Movies, id=movie_id)
    print('reached',movie,movie.added_by,request.user)
    if movie.added_by != request.user:
        return redirect('/')
    if request.method == 'POST':
        form = UserAddForm(request.POST or None,request.FILES,instance=movie,user=request.user)
        if form.is_valid():
            form.save()
            print("success")
            return redirect('/')

    else:
        form = UserAddForm(instance=movie)
    return render(request, 'add_movie.html', {'form': form})
@login_required
def MovieDelete(request,movie_id):
    movie = Movies.objects.get(pk=movie_id)
    if movie.added_by != request.user:
        return redirect('/')
    movie.delete()
    return redirect('/usermovie')
@login_required
def MovieUser(request):
    print("dghvadj jsvdhbkj svbdskv k vdskhbvskvdl",request.user)
    movie_list = Movies.objects.all().filter(added_by=request.user)
    print(movie_list)
    # print(movie_list.object_list)
    return render(request,'movies.html',{'movies':movie_list})
def review(request):
    rev = Review.objects.all()
    return render(request, 'blog.html',{'review':rev} )
def GenreMovies(request,genre="None"):
    print(genre)
    movie_list = Movies.objects.all().filter(genres=genre)
    return render(request, 'movies1.html', {'movies': movie_list})