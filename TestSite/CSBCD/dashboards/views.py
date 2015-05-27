from django.shortcuts import render, render_to_response, RequestContext
from django.http import JsonResponse
from temperatures.models import Temperature
import time

def home(request):
    return render_to_response("dashboard.html", locals(), context_instance = RequestContext(request))

def ajax1(request):
    temperatures = Temperature.objects.all()
    response_data = {'timestamp': [], 'temperature' : [],}
    
    for temp in temperatures:
        response_data['timestamp'].append(temp.timestamp)
        response_data['temperature'].append(temp.value)
	
    return JsonResponse(reponse_data)

def ajax(request):
    temperatures = Temperature.objects.all()
    response_data = {'timestamp' : [], 'value' : [],}

    for temp in temperatures:
        response_data['timestamp'].append(temp.get_epoch())
        response_data['value'].append(temp.get_tempF()) 

    return JsonResponse(response_data)

def ajax2(request):
    temperatures = Temperature.objects.all()
    reponse_data = {'temp': []}
   
    response_data['temp'].append([0, 1])
    response_data['temp'].append([1, 2])
    return JsonResponse(response_data)    
