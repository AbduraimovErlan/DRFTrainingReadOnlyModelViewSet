from django.shortcuts import render
from ReadOnlyModelViewSet1.serializers import SerializersBook1
from ReadOnlyModelViewSet1.models import Book1
from rest_framework import viewsets



class ReadOnlyModelViewSetBook1(viewsets.ReadOnlyModelViewSet):
    queryset = Book1.objects.all()
    serializer_class = SerializersBook1
    lookup_field = 'id'
