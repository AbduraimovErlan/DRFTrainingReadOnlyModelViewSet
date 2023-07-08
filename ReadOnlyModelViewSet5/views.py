from django.shortcuts import render
from ReadOnlyModelViewSet5.models import Book5
from ReadOnlyModelViewSet5.serializers import SerializersBook5
from rest_framework import viewsets


class ReadOnlyModelViewSetBook5(viewsets.ReadOnlyModelViewSet):
    queryset = Book5.objects.all()
    serializer_class = SerializersBook5
    lookup_field = 'id'