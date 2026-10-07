from django.urls import path

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
]


app_name = "cinema"

router = DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns += router.urls
