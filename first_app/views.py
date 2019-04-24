from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  dictionary = {
    'help_need' : 'Help needed here !'
  }
  return render(request, 'first_app/index.html', dictionary)
# Create your views here.
