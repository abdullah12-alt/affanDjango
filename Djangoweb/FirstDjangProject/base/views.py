from django.shortcuts import render
from django.http import HttpResponse
from .models import contact
# Create your views here.
def home(request):
    return render(request,"index.html")

def Contact(request):
    return render(request,'contact.html')