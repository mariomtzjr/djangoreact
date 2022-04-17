from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie-list')

urlpatterns = router.urls