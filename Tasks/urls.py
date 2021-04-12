from django.urls import path
from rest_framework_nested import routers
from Tasks.views import TaskViewSet, BucketViewSet

router = routers.DefaultRouter()
router.register('bucket', BucketViewSet)
router.register('tasks', TaskViewSet)
# tasks_router = routers.NestedDefaultRouter(router, 'tasks_list', lookup='task_list')
# tasks_router.register('tasks', TaskViewSet, basename="tasks")

app_name = "tasks"
urlpatterns = [
    *router.urls,
    # *tasks_router.urls,
]
