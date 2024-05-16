from django.urls import path 
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('login/',login, name="login"),
    path('signup/', views.signup, name="signup"),
   # path('delete/', delete, name="delete"),
    path('logout/', LogoutView.as_view(template_name = 'biblesearch/logout.html'), name="logout"),
]