from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def detail(request, user_id):
    return HttpResponse("You're looking at question %s." % user_id)

def reset(request, user_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % user_id)

def update(request, user_id):
    return HttpResponse("You're voting on question %s." % user_id)

def home(request):
    return render(request, 'index.html')
