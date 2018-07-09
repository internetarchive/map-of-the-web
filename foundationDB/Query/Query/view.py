from django.shortcuts import render
from django.shortcuts import render_to_response
from Query.query import query

def processing(string):
	return string

def test(request):
	queryy = request.GET.get('q','') 
	if queryy:
		fig = query(queryy)
		return render(request, 'test01.html', {'results': fig})
	else:
		results = []
		return render_to_response('test01.html', {'results': results})

