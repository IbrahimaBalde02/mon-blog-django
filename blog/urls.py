from django.urls import path
from .views import req_indexblog,req_article

urlpatterns = [
    path('', req_indexblog, name='blog-index'),
    path('article<str:numeroArticle>/',req_article, name='article'), #<str:numeroArticle>: nous permet de recuperer dynamiquement le numero de l'article a afficher (car nous en avons trois)

]