from django.urls import path
from rest_framework import routers
from Tasks.views import TaskViewSet, TaskListViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('tasks_list', TaskListViewSet)

app_name = "tasks"
urlpatterns = [
    *router.urls
]
