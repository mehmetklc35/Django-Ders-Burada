from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
]
