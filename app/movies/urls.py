"""

"""

from django.urls import path
from rest_framework import routers

from movies import views

router = routers.SimpleRouter()
router.register(r"movies", views.MoviesViewSet)

urlpatterns = router.urls
# [
#     path('movies/', views.MovieList.as_view(), name="create-movie"),
#     path('movies/<int:pk>', views.MovieDetail.as_view(), name="retrieve-movie"),
# ]
