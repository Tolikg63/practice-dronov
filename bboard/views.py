from django.http import HttpResponse


def index(request):
   return HttpResponse("The news are coming!!!")


