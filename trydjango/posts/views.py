from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator

from .models import *
from .forms import *

# Create
def posts_create(request):
    form = PostForm(request.POST or None, request.FILES or None)

    # To save posts in database
    if form.is_valslug():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('title'))
        instance.save()
        messages.success(request,'Successfully Created')
        return HttpResponseRedirect(instance.get_absolute_url())

    # # Stuff gets printed in console
    # if request.method == 'POST':
    #     print(request.POST.get('title'))
    #     print(request.POST.get('content'))

    context = {
        'form': form,
    }
    return render(request,'post_form.html',context)

# Retrieve
def posts_detail(request, slug):
    # instance = Post.objects.get(slug=5)
    instance = get_object_or_404(Post, slug=slug)
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

    queryset_list = Post.objects.all() #.order_by('-timestamp')
    paginator = Paginator(queryset_list, 6) # Show 5 contacts per page

    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    context = {
        'object_list' : queryset,
        'title' : 'List'
    } 
    return render(request,'post_list.html',context)

#Update
def posts_update(request, slug=None):

    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)

    # To save posts in database
    if form.is_valslug():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Updated!')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title' : instance.title,
        'instance' : instance,
        'form' : form,
    }
    return render(request,'post_form.html',context)

# Delete
def posts_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request,'Deleted!')
    return redirect('list')
