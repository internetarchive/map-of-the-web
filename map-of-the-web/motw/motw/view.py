from django.shortcuts import render
from django.shortcuts import render_to_response
from bokeh.resources import CDN
from bokeh.embed import components
import django_tables2 as tables

def test(request):
	query = request.GET.get('q','') 
	if query:
		return render(request, 'test01.html')
	else:
		results = []
		return render_to_response('test01.html', {'results': results})
