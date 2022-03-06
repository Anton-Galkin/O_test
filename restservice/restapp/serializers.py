from rest_framework import serializers
from .models import Object


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('id', 'name', 'type', 'parent')


