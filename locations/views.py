# Create your views here.
from django.http import HttpResponse
from locations.models import Locations
from serializers import ModelSerializer
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render_to_response
from django.template import RequestContext

def locationJSON(request):
    locations = Locations.objects.all()
    data = LocationSerializer().serialize('json', locations)
    callback = request.GET.get('callback')
    if callback:
        data = '%s(%s)' % (callback, data)
    return HttpResponse(data, mimetype='application/json')

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Locations
        exclude = ('id',)
        nested = 1
        
def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

@requires_csrf_token
def processJSON(request):
    newLocation = Locations(locationName = request.POST['locationName'], latitude = request.POST['latitude'], longitude = request.POST['longitude'], locationAddress = request.POST['locationAddress'])
    newLocation.save()
    locations = Locations.objects.all();
    data = LocationSerializer().serialize('json', locations)
    return HttpResponse(data, mimetype='application/json')

    


