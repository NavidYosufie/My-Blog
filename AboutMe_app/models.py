from django.db import models

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
    body = models.TextField()

