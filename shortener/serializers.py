from rest_framework import serializers
from .models import ShortURL

class ShortURLSerialize(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['id', 'url', 'short_code', 'created_at', 'updated_at', 'access_count']
        extra_kwargs = {
            'short_code': {'required': False},  # Make short_code optional
        }