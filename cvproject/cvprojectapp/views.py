from django.shortcuts import render

from django.shortcuts import render
from .models import Profile

# Create your views here.

def accept(request):
  return render(request, '../templates/cvform.html')