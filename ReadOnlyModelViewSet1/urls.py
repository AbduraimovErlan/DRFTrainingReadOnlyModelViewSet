from django.urls import path
from ReadOnlyModelViewSet1 import views



urlpatterns = [
    path('books1/', views.ReadOnlyModelViewSetBook1.as_view({'get': 'list'})),
    path('books1/<int:id>/', views.ReadOnlyModelViewSetBook1.as_view({'get': 'retrieve'}))
]