from django.contrib import admin

from myapp.models import Category, ContactForm, News, OurWorks, Partner

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")


@admin.register(News)
class NewsmAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(OurWorks)
class OurWorksAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "short_description", "phone")
    
    