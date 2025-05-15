from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=35)
    slug = models.SlugField()

    class Meta():
        verbose_name = "Category"

    def __str__(self):
        return self.name
class TableBlog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=True)
    date = models.DateField(default=timezone.now)
    content = models.TextField()
    description = models.TextField()
    class Meta():
        verbose_name = "Article" #affiche article a la TableBlog
        ordering =["-title"]   #une liste qui permet de trier par titre, on peut mettre plusieurs attributs
    def __str__(self):      #surcharge la class pour afficher les titres
        return self.title
    @property       #cette propriété permet de compter le nombre de mot par article après on ajoute cette methode sur le touple list_display qui est dans admin.py,pour que ça marche
    def nombre_mot(self):
        return len(self.content.split())