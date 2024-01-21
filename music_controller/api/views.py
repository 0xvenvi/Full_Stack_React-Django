from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# End point - location of webserver we are going to /


def main(request):
    return HttpResponse("<h1>Hello</h1>")
