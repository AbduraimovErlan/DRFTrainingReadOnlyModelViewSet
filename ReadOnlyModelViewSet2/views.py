from django.shortcuts import render
from ReadOnlyModelViewSet2.serializers import SerializersBook2
from ReadOnlyModelViewSet2.models import Book2
from rest_framework import viewsets


class ReadOnlyModelViewSetBook2(viewsets.ReadOnlyModelViewSet):
    queryset = Book2.objects.all()
    serializer_class = SerializersBook2
    lookup_field = 'id'
