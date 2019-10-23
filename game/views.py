from django.http import HttpResponse


def index(request):
    return HttpResponse("This one is the demonstration of the fact that Dimas has created an app")
