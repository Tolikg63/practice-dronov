from django.http import HttpResponse
from django.shortcuts import render
from .models import Bb


def index(request):
   data = {
      'list': Bb.objects.all()
   }
   return render(request, 'bboard/index.html', context=data)
