from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.list import ListView

from .models import Post


def url_view(request):
    print('url_view()')
    data = {'code': '001', 'msg': 'ok'}
    return HttpResponse('<h1> url_veiw')
    #return JsonResponse()

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username : {username}')
    print(f'request.GET : {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
   
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')


class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'
    

