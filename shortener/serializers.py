from rest_framework import serializers
from .models import ShortURL

class ShortURLSerialize(serializers.ModelSerializer):
    class Meta:
        model=ShortURL
        field=['id','url','short_code','created_at','update_at','access_count']