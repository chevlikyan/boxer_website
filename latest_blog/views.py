from django.shortcuts import render

from latest_blog.models import Blog


# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'home.html', context)
