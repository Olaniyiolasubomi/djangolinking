from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render (request, 'testlink/index.html')
def contact(request):
    return render (request, 'testlink/contact.html')
def about(request):
    return render (request, 'testlink/about.html')
def blog(request):
    return render (request, 'testlink/blog.html')