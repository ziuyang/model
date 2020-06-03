from django.shortcuts import render
from .models import Article
from .models import Blog

# Create your views here.
def home(request):
    article = Article.objects
    blog = Blog.objects
    return render(request, 'home.html', {'article':article, 'blog':blog})