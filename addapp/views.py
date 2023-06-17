from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  home(request):
    return render(request,'home.html')
def add(request):
    X=request.GET["G1"]
    Y=request.GET["G2"]
    i=int(X)
    j=int(Y)
    z=i+j
    res=HttpResponse("THE SUM IS:"+str(z))
    return res
