from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
# def posts_home(request):
#     return HttpResponse('<h1> Hello </h1>')

# Create
def posts_create(request):
    return HttpResponse('<h1> Create </h1>')

# Retrieve
def posts_detail(request, id):
    # instance = Post.objects.get(id=5)
    instance = get_object_or_404(Post, id=id)
    context = {
        'title' : instance.title,
        'instance' : instance
    }
    return render(request,'post_detail.html',context)

#List Items
def posts_list(request):

    # if request.user.is_authenticated():
    #     context = {
    #         'title' : 'User List'
    #     }
    # else:

    queryset = Post.objects.all()
    
    context = {
        'object_list' : queryset,
        'title' : 'List'
    } 
    return render(request,'index.html',context)
    # return HttpResponse('<h1> List </h1>')

#Update
def posts_update(request):
    return HttpResponse('<h1> Update </h1>')

# Delete
def posts_delete(request):
    return HttpResponse('<h1> Delete </h1>')