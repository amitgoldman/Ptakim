from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Tasks",
        default_version='v1',
        description="THE BEST TASKS PROJECT",
        contact=openapi.Contact(email="amitTheKing@king.org"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('tasks/', include('Tasks.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]



