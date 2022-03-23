import re
from django.contrib import admin

from myapp.models import ContactForm, News, OurWorks, WorkImages, Banner
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "subject","email", "created_at")
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False


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
