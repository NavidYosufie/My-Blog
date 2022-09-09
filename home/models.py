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
    image = models.ImageField(upload_to="article/imag", null=True, blank=True)
    body = models.TextField(blank=True)
    
    title_1 = models.CharField(max_length=50)
    body_1 = models.TextField()
    image_body_1 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_2 = models.CharField(max_length=50)
    body_2 = models.TextField()
    image_body_2 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_3 = models.CharField(max_length=50, blank=True)
    body_3 = models.TextField()
    image_body_3 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_4 = models.CharField(max_length=50, blank=True)
    body_4 = models.TextField(blank=True)
    image_body_4 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_5 = models.CharField(max_length=50, blank=True)
    body_5 = models.TextField(blank=True)
    image_body_5 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_6 = models.CharField(max_length=50, blank=True)
    body_6 = models.TextField(blank=True)
    image_body_6 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_7 = models.CharField(max_length=50, blank=True)
    body_7 = models.TextField(blank=True)
    image_body_7 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_9 = models.CharField(max_length=50, blank=True)
    body_9 = models.TextField(blank=True)
    image_body_9 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_10 = models.CharField(max_length=50, blank=True)
    body_10 = models.TextField(blank=True)
    image_body_10 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_11 = models.CharField(max_length=50, blank=True)
    body_11 = models.TextField(blank=True)
    image_body_11 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_12 = models.CharField(max_length=50, blank=True)
    body_12 = models.TextField(blank=True)
    image_body_12 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_13 = models.CharField(max_length=50, blank=True)
    body_13 = models.TextField(blank=True)
    image_body_13 = models.ImageField(upload_to="article/imag", null=True, blank=True)
    
    title_14 = models.CharField(max_length=50, blank=True)
    body_14 = models.TextField(blank=True)
    image_body_14 = models.ImageField(upload_to="article/imag", null=True, blank=True)

    

    cateqory = models.ManyToManyField(Cateqory)
    tip = models.TextField(blank=True)
 
    created = models.DateField(default=timezone.now())
    



    def __str__(self) -> str:
        return self.title


class Coment(models.Model):
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    nomber_massage = models.IntegerField(default=0)

    
    def __str__(self) -> str:
        return f"{self.name}  -  {self.message[:30]}"
