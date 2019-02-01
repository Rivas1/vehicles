from django.shortcuts import render
from django.http import HttpResponse

from .models import Vehicles
# Create your views here.
def index ( request ):
	# return HttpResponse('Hello from Vehicles!')

	vehicles = Vehicles.objects.all()[:10]

	context = {
		'title': 'Latest Vehicles',
		'vehicles': vehicles

	}

	return render (request, 'vehicles/index.html', context)

def details ( request, id ):
	vehicle = Vehicles.objects.get(id=id)

	context = {
		'vehicle': vehicle

	}

	return render (request, 'vehicles/details.html', context)