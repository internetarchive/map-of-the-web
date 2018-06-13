from django.shortcuts import render
from django.shortcuts import render_to_response
from mysite.producing import processing
from mysite.producing import Count
from mysite.producing import download
from bokeh.resources import CDN
from bokeh.embed import components
import django_tables2 as tables

class SimpleTable(tables.Table):
	timestamp = tables.Column()
	usefulness = tables.Column()
	same_as = tables.Column()

def test(request):
	query = request.GET.get('q','') 
	if query:
		fig = processing(query)
		total_number = Count(query)
		script1, div1 = components(fig[0], CDN)
		script2, div2 = components(fig[1], CDN)
		queryset = fig[2]
		querydict = [{'timestamp':q['timestamp'], 'usefulness':q['usefulness'], 'same_as':q['same_as']} for q in queryset]
		table = SimpleTable(querydict)
		table.paginate(page=request.GET.get('page', 1), per_page=25)
		return render(request, 'test01.html', \
									{'script1': script1, 'div1': div1, \
									 'script2': script2, 'div2': div2, \
									 'results': query, 'total_number': total_number, \
									 'table': table})
	else:
		results = []
		return render_to_response('test01.html', {'results': results})
