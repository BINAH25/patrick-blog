from django.views.generic import TemplateView
from .models import Message, Post
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


def send(request):
    email = request.POST['email']

    user= Message.objects.create(email=email)
    user.save()
    return HttpResponse('Subcription successful')


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})

