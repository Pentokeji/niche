from django.shortcuts import render,HttpResponse

# Testing View, will dissapear later.
def index(request):
    return HttpResponse("We can keep track of all the plants here.")

