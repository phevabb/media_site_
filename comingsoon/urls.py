
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name="home"),
    path('index.html',views.index, name="index"),
    path('index.html',views.news_let, name="news_let")
]
