from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string, get_template
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from .models import Pokemon, Trainers
import csv

# Create your views here.
def index(request): 
	return render(request, "pokemon/index.html")

def about(request): 
	return render(request, "pokemon/about.html") 

def trainers(request): 
	# trainer_classes = Trainers().objects.all()
	trainer_classes = []
	with open("trainers.csv") as trainers_csv:
		trainer_list = csv.reader(trainers_csv)
		for row in trainer_list:
			trainer_classes.append(row)
	return render(request=request, template_name="pokemon/trainers.html", context={'trainer_classes': trainer_classes})
