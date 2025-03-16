import validators 
import requests 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404,redirect
from .models import ShortURL
from .serializers import ShortURLSerialize
import random
import string

def generate_short_code():
    """Generate a random 6-character short code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortenURL(APIView):
    def post(self, request):
        """Create a short URL for a given long URL."""
        url = request.data.get('url')

        # Check if the URL is provided
        if not url:
            return Response(
                {"error": "URL is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the URL is valid
        if not validators.url(url):
            return Response(
                {"error": "Invalid URL format."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the URL exists
        try:
            response = requests.head(url, timeout=5)
            if response.status_code != 200:
                return Response(
                    {"error": "URL does not exist or is unreachable."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except requests.RequestException:
            return Response(
                {"error": "URL does not exist or is unreachable."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Generate a unique short code
        short_code = generate_short_code()
        while ShortURL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()

        # Save the URL and short code
        short_url = ShortURL.objects.create(
            url=url,
            short_code=short_code
        )

        # Return the response
        serializer = ShortURLSerialize(short_url)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class RedirectToOriginalURL(APIView):
    def get(self, request, short_code):
        """Redirect to the original URL using the short code."""
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.access_count += 1  # Increment access count
        short_url.save()
        return redirect(short_url.url)
class RetrieveURL(APIView):
    def get(self, request, short_code):
        """Retrieve the original URL using the short code."""
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.access_count += 1  # Increment access count
        short_url.save()
        serializer = ShortURLSerialize(short_url)
        return Response(serializer.data)

class UpdateURL(APIView):
    def put(self, request, short_code):
        """Update an existing short URL."""
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerialize(short_url, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteURL(APIView):
    def delete(self, request, short_code):
        """Delete an existing short URL."""
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class URLStats(APIView):
    def get(self, request, short_code):
        """Get access statistics for a short URL."""
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerialize(short_url)
        return Response(serializer.data)