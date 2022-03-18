from django.contrib import admin

from myapp.models import ContactForm, News, OurWorks, WorkImages, Banner

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")


@admin.register(News)
class NewsmAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at",)



class WorkImagesAdmin(admin.StackedInline):
    model = WorkImages
    extra = 1   
    max_num= 4
@admin.register(OurWorks)
class OurWorksAdmin(admin.ModelAdmin):
    inlines = [WorkImagesAdmin]
    list_display = ("title",  "created_at")
    class Meta:
        model = OurWorks


@admin.register(Banner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("title",)
