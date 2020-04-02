"""

"""

from rest_framework import routers

from movies import views

router = routers.SimpleRouter()
router.register(r"movies", views.MoviesViewSet)

urlpatterns = router.urls
