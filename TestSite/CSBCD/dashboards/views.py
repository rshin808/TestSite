from django.shortcuts import render, render_to_response, RequestContext
from django.http import JsonResponse
from temperatures.models import Temperature 


def home(request):
    return render_to_response("dashboard.html", locals(), context_instance = RequestContext(request))

def temperatures(request):
    response_data = {
        'timestamp' : [],
        'value' : {
                    'tempF': [],
                    'tempC': [],
                    'tempK': [],    
                  },
    }
    temperatures = Temperature.objects.all()

    for temperature in temperatures:
        response_data['timestamp'].append(temperature.get_epoch())
        response_data['value']['tempF'].append(temperature.get_tempF())
        response_data['value']['tempC'].append(temperature.get_tempC())
        response_data['value']['tempK'].append(temperature.get_tempK())
    
    return JsonResponse(response_data) 
