from django.contrib import admin
from django.urls import path, include  # include is required to reference app urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the API app routes
    path('api/', include('api.urls')),  # all endpoints from api/urls.py will be under /api/
]
