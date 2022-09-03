from email import message
from django.shortcuts import render
from .models import Information, Contact_my, Cv_my, Article, Coment




def about(request):  
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        body = request.POST.get("message")
        Contact_my.objects.create(fullName=name, email=email, body=body)

    information = Information.objects.all()
    my_cv = Cv_my.objects.all()

    articles = Article.objects.all()
        

    return render(request, 'index.html', context={"about_me": information, "show_cv": my_cv, "articels": articles})




def article(request, id):
    article = Article.objects.get(id=id)
    
    return render(request, "blog-post.html", context={"articles": article})

