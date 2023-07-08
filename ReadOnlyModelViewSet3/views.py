from django.shortcuts import render
from ReadOnlyModelViewSet3.models import Book3
from ReadOnlyModelViewSet3.serializers import SerializersBook3
from rest_framework import viewsets



class ReadOnlyModelViewSetBook3(viewsets.ReadOnlyModelViewSet):
    queryset = Book3.objects.all()
    serializer_class = SerializersBook3
    lookup_field = 'id'