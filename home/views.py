from blog.models import Post
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

class aboutview(TemplateView):
    template_name='home/about.html'



def search(request):

    query= request.GET['query']
    if len(query)>78:
        allPosts= Post.objects.none()

    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts= allPostsTitle.union(allPostsContent)

    if allPosts.count()==0:
        messages.warning(request,"No search result found. Please refine your search")
    params = {'allPosts':allPosts,'query':query}

    return render(request,'home/search.html',params)


    

