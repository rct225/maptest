# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.core import serializers
from locations.models import Locations

def index(request):
    return HttpResponse("Hello World!")

def locationJSON(request):
    locations = Locations.objects.all()
    data = serializers.serialize('json', locations)
    return HttpResponse(data, mimetype='application/json')
