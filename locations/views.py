# Create your views here.
from django.http import HttpResponse
from locations.models import Locations
from serializers import ModelSerializer


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
    return HttpResponse("Hello World!")


