from django.urls import path
from rest_framework import routers

from users.views import UserViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet)


app_name = "users"
urlpatterns = [
    *router.urls,
]
