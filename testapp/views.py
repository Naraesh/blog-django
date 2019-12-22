from django.shortcuts import render
from django.views.generic import ListView
from post.models import authorpost
# Create your views here.
def about(request):
    return render(request,'about.html')

def index(request):
    context = authorpost.objects.all()
    return render(request,'base.html',{'posts':context})

def myfeed(request):
    context = authorpost.objects.all()
    return render(request, 'myfeeds.html',{'feed':context})
        
class Post(ListView):
    model= authorpost
    template_name='base.html'
    context_object_name='posts'
    ordering=['date_published']