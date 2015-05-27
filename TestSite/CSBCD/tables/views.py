from django.shortcuts import render, render_to_response, RequestContext
from django.http import JsonResponse

def table(request):
    return render_to_response("tables.html", locals(), context_instance = RequestContext(request))

def temperature_json(request):
    return JsonResponse({"foo":"bar"})
