from django.shortcuts import render
from django.http import HttpResponse
def homepage(request):
    return render(request,'home.html',{'name':'fekk'})
def biodata(request):
    return HttpResponse('<h1> this is my data<h1>')
def count(request):
    data =request.GET['fulltextarea']

    
    return render(request,'count.html',{'fulltext':data})