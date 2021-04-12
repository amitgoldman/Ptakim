from django.urls import path
from rest_framework import routers
from Tasks.views import TaskViewSet

router = routers.DefaultRouter()
router.register('', TaskViewSet)

app_name = "tasks"
urlpatterns = [
    *router.urls
]
