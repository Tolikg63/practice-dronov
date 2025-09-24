from django.http import HttpResponse
from django.shortcuts import render
from .models import Bb


def index(request):
   # bbs = Bb.objects.order_by('-publish')
   data = {
      'list': Bb.objects.order_by('-publish')
   }
   return render(request, 'bboard/index.html', context=data)
