from django.shortcuts import render
from .models import places
from .models import team
# Create your views here.
def start(request):
    obj=places.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{"key1":obj,"key2":obj1})