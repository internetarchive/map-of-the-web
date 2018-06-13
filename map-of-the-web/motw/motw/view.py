from django.shortcuts import render
from django.shortcuts import render_to_response
from motw.producing import Count

def test(request):
	query = request.GET.get('q','') 
	if query:
		total_number = Count(query)
		return render(request, 'test01.html', \
									{'results': query, 'total_number': total_number})
	else:
		results = []
		return render_to_response('test01.html', {'results': results})
