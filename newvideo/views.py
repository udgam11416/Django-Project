

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import CategoryList,Item,CommentVideo

from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib import messages
from django.urls import reverse
from newvideo.templatetags import extras


# Create your views here.

# def categorylist(request):
#     categories=CategoryList.objects.all()
#     return render(request,'newvideo/categorylist.html',{'category':categories})

class categorylist(ListView):
    model=CategoryList
    context_object_name='category'
    template_name='newvideo/categorylist.html'



# def category_view(request,category_slug):
#     category_name= CategoryList.objects.filter(slug=category_slug).first()
#     # category= get_object_or_404(CategoryList,slug=category_slug)
#     article=Item.objects.filter(category=category_name)
#     context={'article':article,'category':category_name}
#     return render(request,'newvideo/categoryview.html',context)

class categoryviews(ListView):
    template_name='newvideo/categoryview.html'
    context_object_name='article'


    def get_queryset(self):
        self.category=get_object_or_404(CategoryList,slug=self.kwargs
        ['category_slug'] ) #{category_slug:c.slug}
        return Item.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):      #args  #kwargs
        context = super().get_context_data(**kwargs)
        context['category']=self.category
        return context



# class ArticleDetail(DetailView):
#     slug_url_kwarg= 'article_slug'
#     model=Item
#     template_name='newvideo/articledetail.html'
#     context_object_name='article'



def article_detail(request,article_slug):
    article=Item.objects.filter(slug=article_slug).first()
    comments = CommentVideo.objects.filter(article=article,parent=None)
    replies= CommentVideo.objects.filter(article=article).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.srno not in repDict.keys():
            repDict[reply.parent.srno]=[reply]
        else:
            repDict[reply.parent.srno].append(reply)

    context={'article':article,'comments':comments,'user':request.user,'repDict':repDict}
    print(request.user)
    return render (request,'newvideo/articledetail.html',context)






    # return render(request,'newvideo/articledetail.html',{'article':article})


def postComment(request):
    print("hi")
    if request.method=="POST":
        print("hi")
        comment=request.POST.get("desc")
        user1=request.user
        articleSno=request.POST.get("articleSno")
        article=Item.objects.get(sno=articleSno)
        parentSno=request.POST.get("parentSno")
        if parentSno=="":
            # print(comment,"\n",user,"\n",articleSno)
            comment1 = CommentVideo(desc=comment,username=user1,article=article)
            comment1.save()
            messages.success(request,"Your comment has been posted successfully")

        else:
            parent_comment = CommentVideo.objects.get(srno=parentSno)
            comment2 = CommentVideo(desc=comment,username=user1,article=article,parent=parent_comment)
            

            comment2.save()
            messages.success(request,"Your reply has been posted successfully")



    return HttpResponseRedirect(reverse('newvideo:articledetail',args=(article.slug,)))











