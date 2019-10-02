from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def posts_home(request):
#     return HttpResponse('<h1> Hello </h1>')

# Create
def posts_create(request):
    return HttpResponse('<h1> Create </h1>')

# Retrieve
def posts_detail(request):
    return HttpResponse('<h1> Detail </h1>')

#List Items
def posts_list(request):
    return HttpResponse('<h1> List </h1>')

#Update
def posts_update(request):
    return HttpResponse('<h1> Update </h1>')

# Delete
def posts_delete(request):
    return HttpResponse('<h1> Delete </h1>')