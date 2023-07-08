from django.shortcuts import render
from ReadOnlyModelViewSet4.models import Book4
from ReadOnlyModelViewSet4.serializers import SerializersBook4
from rest_framework import viewsets




class ReadOnlyModelViewSetBook4(viewsets.ReadOnlyModelViewSet):
    queryset = Book4.objects.all()
    serializer_class = SerializersBook4
    lookup_field = 'id'
