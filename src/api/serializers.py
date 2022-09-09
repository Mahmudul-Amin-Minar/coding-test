import imp
from rest_framework import serializers
from django.contrib.auth.models import User

from shortener.models import ShortenUrl

class ShortenUrlSerializer(serializers.ModelSerializer):
    class Meta:
        pass