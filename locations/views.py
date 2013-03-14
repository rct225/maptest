# Create your views here.
from django.http import HttpResponse
from locations.models import Locations
from serializers import ModelSerializer
from django.utils import simplejson
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
    data = simplejson.loads(request.POST['action'])
    return HttpResponse(data, mimetype='application/json')
    


