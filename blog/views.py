from django.shortcuts import render
from datetime import datetime

def req_indexblog(request):
    date = datetime.today()
    heure = datetime.now().time()
    return render(request, 'blog/index.html',context={'date':date,'heure':heure})
def req_article(request,numeroArticle):     #le deuxieme argument c'est pour le numero de l'article a afficher
    if numeroArticle in ["1","2","3"]:
        return render(request, f'blog/article{numeroArticle}.html',context={}) #on a utiliser le fstring pour afficher l'article avec son numero
    return render(request,'blog/page_not_found.html')
