from django.shortcuts import render, render_to_response, RequestContext
from django.http import JsonResponse
from temperatures.models import Temperature 


def home(request):
    return render_to_response("dashboard.html", locals(), context_instance = RequestContext(request))

def temperatures(request):
    response_data = {
        'timestamp' : [],
        'value' : [],
    }
    temperatures = Temperature.objects.all()

    for tempF in temperatures:
        response_data['timestamp'].append(tempF.get_epoch())
        response_data['value'].append(tempF.get_tempF())
    
    return JsonResponse(response_data) 
