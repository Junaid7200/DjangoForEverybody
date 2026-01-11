from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def simpleView(request):
	return HttpResponse("Silence is a true friend who never betrays.")
