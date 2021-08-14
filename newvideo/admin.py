from django.contrib import admin
from .models import CategoryList,Item,CommentVideo
from embed_video.admin import AdminVideoMixin


# Register your models here.

admin.site.register((CategoryList,CommentVideo))

class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass



admin.site.register(Item,MyModelAdmin)



