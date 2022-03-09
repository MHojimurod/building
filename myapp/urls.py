from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('news/',news,name="news"),
    path('works/',works,name="works"),
    path('works/',works,name="works"),
    path('about_company/',about_company,name="about_company"),
    path('mission/',mission,name="mission"),
]