from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed, ResponseHeaders
from django.shortcuts import render
from django.http import HttpResponse

from .templates.forms import EventForm
from .utils import events_collection
import pprint
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bson import json_util
# Create your views here.
def parse_json(data):
    return json.loads(json_util.dumps(data))
def index(request):
    return HttpResponse("Hello there")
@csrf_exempt
def add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if not form.is_valid():
            return render(request,'detailsform.html',{'form':EventForm(),'message':'Incorrect Details... Please correct and try again'})
        e = {}
        for key in form.cleaned_data:
            e[key] = request.POST[key]
        try:
            events_collection.insert_one(e)
        except:
            print('ERRORRRRR')
        return render(request,'detailsform.html',{'form':EventForm(),'message':'Details added successfully'})
    elif request.method == 'GET':
        return render(request,'detailsform.html',{'form':EventForm()})
def getEvents(request):
    if request.method == 'GET':
        resp = []
        try: 
            events = events_collection.find() 
            for event in events:
                pprint.pprint(event)
                resp.append(parse_json(event))
        except:
            print('Couldn\'t get from db')
            return HttpResponseBadRequest('Couldn\'t get events')
        return JsonResponse({"data":resp})