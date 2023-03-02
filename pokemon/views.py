from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
def index(request): 
	return render(request, "pokemon/index.html")