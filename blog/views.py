from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from blog.models import Post
from django.contrib import messages
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse



def bloghome(request):

    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)







def blogpost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
       is_liked = True
    return render(request, 'blog/blogPost.html', {'post': post, 'is_liked': is_liked, 'total_likes': post.total_likes(), })   
    
 
def like_post(request):

    post = get_object_or_404(Post, id=request.POST.get('id'))    
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('blog/like-section.html', context, request=request)
        return JsonResponse({'form': html})









    
    

# Create your views here.
