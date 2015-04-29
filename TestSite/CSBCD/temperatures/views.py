from django.shortcuts import render
from django.http import HttpResponse
from .models import Temperature
from django.http import JsonResponse

def chart_data_json(request):
    return JsonResponse({"foo": "bar"})    
