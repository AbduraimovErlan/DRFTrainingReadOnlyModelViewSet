from django.urls import path
from ReadOnlyModelViewSet5 import views





urlpatterns = [
    path('books5/', views.ReadOnlyModelViewSetBook5.as_view({'get': 'list'})),
    path('books5/<int:id>/', views.ReadOnlyModelViewSetBook5.as_view({'get': 'retrieve'})),
]