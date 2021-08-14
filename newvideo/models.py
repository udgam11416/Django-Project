from django.db import models
from embed_video.fields import EmbedVideoField
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now




# Create your models here.
class CategoryList(models.Model):
    name=models.CharField(unique=True,max_length=50)
    img=models.ImageField(upload_to='categorypics',blank=True)
    slug=models.SlugField(max_length=60,unique=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name

class Item(models.Model):
    sno = models.AutoField(primary_key = True)
    title=models.CharField(max_length=100)
    category=models.ForeignKey(CategoryList,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='videothumbnail',blank=True)
    slug=models.SlugField(unique=True,max_length=50)
    desc=models.TextField()
    video=EmbedVideoField()
    publish=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-title',)
    
    def __str__(self):
        return self.title


class CommentVideo(models.Model):
    desc=models.TextField()
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    srno=models.AutoField(primary_key=True)
    article=models.ForeignKey(Item,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)


    def __str__(self):
        return self.desc[0:10] + "..." + "by" + self.user.username



    

    
