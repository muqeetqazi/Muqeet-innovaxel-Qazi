from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the URL Shortener API! we have connect with SQL too"})
