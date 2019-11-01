from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^index/', views.index),
    url(r'^getstudents/', views.get_students),
    url(r'^temp/', views.temp),
    url(r'^home/', views.home),
    url(r'^hehe', views.hehe),
    url(r'^hehehe', views.hehehe),
]