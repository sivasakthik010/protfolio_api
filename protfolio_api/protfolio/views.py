from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getUser(request, email=""):
    print(email)
    return HttpResponse(email)