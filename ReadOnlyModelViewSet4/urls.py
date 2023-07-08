from django.urls import path
from ReadOnlyModelViewSet4 import views




urlpatterns = [
    path('books4/', views.ReadOnlyModelViewSetBook4.as_view({'get': 'list'})),
    path('books4/<int:id>/', views.ReadOnlyModelViewSetBook4.as_view({'get': 'retrieve'}))
]