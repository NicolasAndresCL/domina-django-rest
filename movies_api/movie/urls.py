from django.urls import path

# from movie.views import get_movies, put_movies
from movie.views import MovieAPIView

app_name = "movie"

urlpatterns = [
    path("", MovieAPIView.as_view(), name="movie")
    # path("", get_movies, name="movie"),
    # path("<int:pk>", put_movies, name="movie"),
]
