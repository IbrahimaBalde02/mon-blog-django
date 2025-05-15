from django.urls import path
from .views import req_indexblog,req_articleblog,req_slug

urlpatterns = [
    path('', req_indexblog, name='blog-index'),
    path('article/',req_articleblog, name='blog-article'),
    path('detail/',req_slug, name='blog-detail')

]