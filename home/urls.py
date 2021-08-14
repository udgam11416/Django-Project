from django.urls import path 
from .views import aboutview

from django.views.generic import TemplateView
from home import views


app_name = 'home'
urlpatterns = [
    # path('', views.home, name= 'home'),
    path('',TemplateView.as_view(template_name='home/home.html'), name= 'home'),
    # path('abouttechnews/',views.about, name='about'),
    path('abouttechnews/',aboutview.as_view(), name='about'),
    # path('login/',views.login,name='login'),
    # path('contact/',views.contact,name='contact'),
    # path('help/',views.help,name='help'),
    path('search/',views.search,name='search'),

 ]
