from django.shortcuts import render_to_response, render
from django.template import RequestContext

# Create your views here.


def home(request):

	return render_to_response('index.html', {}, context_instance=RequestContext(request))