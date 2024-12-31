from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('index.html',views.index, name="index"),
]
#This is special url path for handling errors
handler404 = "website.views.error_404_view"