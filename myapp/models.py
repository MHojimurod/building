from distutils.command.upload import upload
from sre_constants import CATEGORY
from django.db import models
from django.core.validators import FileExtensionValidator
val=[FileExtensionValidator(allowed_extensions=['pdf'])]

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=300,verbose_name="Nomi")
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
    title = models.CharField(max_length=128, verbose_name="Nomi")

    def __str__(self) -> str:
        return self.title

class OurWorks(models.Model):
    title = models.CharField(max_length=200,verbose_name="Nomi")
    description = models.TextField(verbose_name="Ma'lumoti")
    photo = models.ImageField(verbose_name="Asosiy rasim",upload_to="images/")
    pdf = models.FileField(verbose_name="Fayl",upload_to="images/",validators=val)
    address = models.CharField(max_length=200,verbose_name="Manzil")
    size = models.IntegerField(verbose_name="Maydoni")
    floor = models.IntegerField(verbose_name="Qavati")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="works", null=True, verbose_name="Kategoriyasi")

    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class WorkImages(models.Model):
    our_works = models.ForeignKey(OurWorks, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="Qo'shimcha rasm",upload_to="images/")

class Partner(models.Model):
    full_name = models.CharField(max_length=128, verbose_name=("To'liq ismi"))
    phone = models.CharField(max_length=128, verbose_name="Telefon raqami")
    short_description = models.TextField(verbose_name="Qisqacha ma'lumoti")
    photo = models.ImageField(upload_to="partners/photo", verbose_name="Rasmi")

    created_at = models.DateField(auto_now_add=True)


