from rest_framework import serializers
from ReadOnlyModelViewSet1.models import Book1



class SerializersBook1(serializers.ModelSerializer):
    class Meta:
        model = Book1
        fields = "__all__"