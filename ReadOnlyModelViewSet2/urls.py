from django.urls import path
from ReadOnlyModelViewSet2 import views



urlpatterns = [
    path('books2/', views.ReadOnlyModelViewSetBook2.as_view({'get': 'list'})),
    path('books2/<int:id>/', views.ReadOnlyModelViewSetBook2.as_view({'get': 'retrieve'})),
]