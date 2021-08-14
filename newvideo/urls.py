from django.urls import path
from . import views
from .views import categorylist,categoryviews


app_name='newvideo'
urlpatterns=[
path('postComment',views.postComment, name='postComment'),
# path('categories/',views.categorylist,name='categorylist'),
path('categories/',categorylist.as_view(),name='categorylist'),
# path('<slug:category_slug>/',views.category_view,name='categoryview'),
path('<slug:category_slug>/',categoryviews.as_view(),name='categoryview'),
path('<slug:article_slug>',views.article_detail,name='articledetail'),
#path('<slug:article_slug>',ArticleDetail.as_view(),name='articledetail'),

]