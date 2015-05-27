from django.shortcuts import render, render_to_response, RequestContext

def chart(request):
    return render_to_response("charts.html", locals(), context_instance = RequestContext(request))
