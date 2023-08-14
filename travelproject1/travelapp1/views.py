from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from .models import team
# Create your views here.
def demo(request):
    x=place.objects.all()
    y=team.objects.all()
    obj={
        'obj1':x,
        'obj2':y}
    return render(request,"index.html",obj)

    # return render(request,"index.html",{'result':y})