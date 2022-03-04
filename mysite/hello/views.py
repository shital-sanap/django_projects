from django.shortcuts import HttpResponse

# Create your views here.

def myview(request):

    num_visits = request.session.get('num_visits',0) + 1

    request.session['num_visits'] = num_visits

    resp = HttpResponse("view count=" + str(num_visits))
    resp.set_cookie('dj4e_cookie','0fb607d8',max_age=1000)
    print(request.COOKIES)
    return resp

