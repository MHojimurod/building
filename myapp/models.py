from distutils.command.upload import upload
from sre_constants import CATEGORY
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=300,verbose_name="Mavzu")
    description = models.TextField(verbose_name="Text")
    photo = models.ImageField(verbose_name="Rasm",upload_to="images/")

    created_at = models.DateTimeField(auto_now_add=True)


class ContactForm(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ismi")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200,verbose_name="Mavzu")
    description = models.TextField(verbose_name="Xabar")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



# class Partners(models.Model):
#     pass


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title



class OurWorks(models.Model):
    title = models.CharField(max_length=200,verbose_name="Nomi")
    photo = models.ImageField(verbose_name="Rasmi",upload_to="images/")
    description = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="works", null=True)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title