from django.urls import path,include
from users import views


app_name='users'

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')

]