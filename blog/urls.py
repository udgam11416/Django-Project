from django.urls import path
from . import views


app_name="blog"

urlpatterns=[

    path('',views.bloghome,name="BlogHome"),
    path('<int:pk>',views.blogpost,name="BlogPost"),
    path('like/', views.like_post, name="like_post"),


]
