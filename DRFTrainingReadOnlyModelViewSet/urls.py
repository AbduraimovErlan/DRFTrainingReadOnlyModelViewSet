from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ReadOnlyModelViewSet1.urls')),
    path('api/v1/', include('ReadOnlyModelViewSet2.urls')),
]
