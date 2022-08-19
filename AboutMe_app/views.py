from django.shortcuts import render
from .models import Information, Contact_my, Cv_my

def about(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        body = request.POST.get("message")
        Contact_my.objects.create(fullName=name, email=email, body=body)

    information = Information.objects.all()
    my_cv = Cv_my.objects.all()

    return render(request, 'index.html', context={"about_me": information, "show_cv": my_cv})






