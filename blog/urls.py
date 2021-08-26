from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('contact', views.ContactPageView.as_view(), name='contact'),
    path('send', views.send, name='send'),
    path ('post/<str:pk>', views.post, name='post'),
]