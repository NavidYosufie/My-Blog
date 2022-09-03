from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


#about my
class Information(models.Model):
    fname = models.CharField(max_length=25, blank=True)
    lname = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    city = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    Phon = models.CharField(max_length=20)
    adderss = models.CharField(max_length=80)
    Imag_profile = models.ImageField()
    description = models.TextField()

    instagram = models.CharField(max_length=60)
    whatsapp = models.CharField(max_length=60)
    github = models.CharField(max_length=60)
    linkedin = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.fname}   -   {self.lname}"



class Contact_my(models.Model):
    fullName = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"{self.fullName}  - {self.body}"



class Cv_my(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title




#articles
class Cateqory(models.Model):
    title = models.CharField(max_length=60)


    def __str__(self) -> str:
        return self.title



class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    
    title_1 = models.CharField(max_length=50)
    image_body_1 = models.ImageField()
    
    title_2 = models.CharField(max_length=50)
    image_body_2 = models.ImageField()
    
    title_3 = models.CharField(max_length=50)
    image_body_3 = models.ImageField()
    
    title_4 = models.CharField(max_length=50)
    image_body_4 = models.ImageField()

    cateqory = models.ManyToManyField(Cateqory)
    body_1 = models.TextField()
    body_2 = models.TextField()
    tip = models.TextField()
    body_3 = models.TextField()
    body_4 = models.TextField()
    created = models.DateField(default=timezone.now())
    image = models.ImageField(upload_to="image/article")



    def __str__(self) -> str:
        return self.title


class Coment(models.Model):
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    nomber_massage = models.IntegerField(default=0)

    
    def __str__(self) -> str:
        return f"{self.name}  -  {self.message[:30]}"
