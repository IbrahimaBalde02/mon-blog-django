from django.shortcuts import render,get_object_or_404
from datetime import datetime

from .models import TableBlog


def req_indexblog(request):
    date = datetime.today()
    heure = datetime.now().time()
    return render(request, 'blog/index.html',context={'date':date,'heure':heure})
def req_articleblog(request):
    articles = TableBlog.objects.all()
    return render(request,'blog/article.html',context={'articles':articles})
def req_slug(request):
    post = TableBlog.objects.get(pk=2)
    return render(request,'blog/page-slug.html',context={'post':post})
