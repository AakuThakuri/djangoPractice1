from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	views = {}
	views['infos'] = Information.objects.all()
	return render(request, 'contact.html' , views)

def portfolio(request):
	return render(request, 'portfolio.html')

def price(request):
	return render(request, 'price.html')

def services(request):
	return render(request, 'services.html')
