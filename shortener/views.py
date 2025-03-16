from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortURL
from .serializers import ShortURLSerialize
import random
import string

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortenURL(APIView):
    def post(self, request):
        serializer = ShortURLSerialize(data=request.data)
        if serializer.is_valid():
            short_code = generate_short_code()
            while ShortURL.objects.filter(short_code=short_code).exists():
                short_code = generate_short_code()
            # Add short_code to the validated data
            serializer.validated_data['short_code'] = short_code
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveURL(APIView):
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.access_count += 1
        short_url.save()
        return Response(ShortURLSerialize(short_url).data)

class UpdateURL(APIView):
    def put(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerialize(short_url, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteURL(APIView):
    def delete(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class URLStats(APIView):
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return Response(ShortURLSerialize(short_url).data)