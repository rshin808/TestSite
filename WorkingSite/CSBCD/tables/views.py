from django.shortcuts import render, render_to_response, RequestContext

def table(request):
    return render_to_response("tables.html", locals(), context_instance = RequestContext(request))
