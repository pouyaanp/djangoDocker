from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>hello this is test for learning dockerising django and mysql<h1>")