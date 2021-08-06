from api.models import Movie
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'desc', 'year')
