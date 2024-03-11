from django.urls import path
from . import views

urlpatterns = [
    path('',views.MovieList,name="MovieList"),
    path('addmovie',views.MovieCreate,name='MovieCreate'),
    path('editmovie/<int:movie_id>', views.MovieEdit, name='MovieEdit'),
    path('deletemovie/<int:movie_id>', views.MovieDelete, name='MovieDelete'),
    path('usermovie/', views.MovieUser, name='MovieUser'),
    path('user_review/',views.review,name='review'),
    path('movies/<slug:genre>/',views.GenreMovies,name='GenreMovies'),
    path('<slug:movie_slug>/',views.MovieDetails,name='MovieDetails'),

]