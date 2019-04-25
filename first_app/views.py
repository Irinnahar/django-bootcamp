from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
  webpage = AccessRecord.objects.order_by('date')
  acc_dict = {
    'access_record': webpage
  }
  return render(request, 'first_app/index.html', acc_dict)
# Create your views here.
