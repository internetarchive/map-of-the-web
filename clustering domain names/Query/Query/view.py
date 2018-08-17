from django.shortcuts import render
from django.shortcuts import render_to_response
#from Query.query import query
from Query.Computing import tf_idf, present

def processing(string):
	return string

def test(request):
	queryy = request.GET.get('q','') 
	if queryy:
		result = tf_idf(queryy)
		fig = present(result)
		#fig2 = processing("accuweather.com")
		return render(request, 'test01.html', {'results': fig})
	else:
		results = []
		return render_to_response('test01.html', {'results': results})

