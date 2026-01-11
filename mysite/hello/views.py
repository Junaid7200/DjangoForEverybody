from django.http import HttpResponse

def helloView(request):
	num_visits = request.session.get("num_visits", 0) + 1
	request.session["num_visits"] = num_visits
	if num_visits > 4:
		del(request.session["num_visits"])
	resp = HttpResponse("b2486eb4<br>view count="+str(num_visits))
	resp.set_cookie('dj4e_cookie', 'fac1f066', max_age=1000)
	return resp
