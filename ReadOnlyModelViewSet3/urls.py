from django.urls import path
from ReadOnlyModelViewSet3 import views



urlpatterns = [
    path('books3/', views.ReadOnlyModelViewSetBook3.as_view({'get': 'list'})),
    path('books3/<int:id>/', views.ReadOnlyModelViewSetBook3.as_view({'get': 'retrieve'})),
]