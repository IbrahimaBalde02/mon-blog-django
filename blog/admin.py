from django.contrib import admin
from .models import TableBlog,Category
@admin.register(TableBlog)
class TableBlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        'published',
        'slug',
        "author",
        "date",
        "nombre_mot",
    )
    empty_value_display = "Inconnue" #permet d'attribuer la valeur 'inconnue' aux articles qui n'ont pas d'auteur
    list_editable = ["published","slug"] #permet de rendre un champ editable
    search_fields = ("title", "slug") #permet d'effectuer une recherche
    list_filter = ("published", "author") #permet de filtrer les champs par 'published ou author'
    autocomplete_fields = ("author",) #permet d'effectuer un filtre sur le champ author lors d'un enregistrement
    list_per_page = 2   #permet de specifier le nombre d'article (objet) à afficher par page, car par defaut django affiche les 100 premiers
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )
