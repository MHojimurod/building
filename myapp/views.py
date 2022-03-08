from unicodedata import name
from django.shortcuts import redirect, render
from .models import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    ctx = {
        "home":"active"
    }
    return render(request, 'main/index.html',ctx)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        description = request.POST["description"]
        contact = ContactForm.objects.create(
            name=name,
            email=email,
            subject=subject,
            description=description
        )
        contact.save()
        messages.success(request, "Rahmat qabul qilindi. Biz sizga tez orada aloqaga chiqamiz !")
        return redirect("contact")
    ctx = {
        "contact":"active"
    }
    return render(request, 'main/contact.html',ctx)

def about(request):
    ctx = {
        "about":"active"
    }
    return render(request, 'main/about.html',ctx)
def news(request):
    ctx = {
        "news":"active"
    }
    return render(request, 'main/news-grid.html',ctx)
def works(request):
    ctx = {
        "works":"active"
    }
    return render(request, 'main/works-grid.html',ctx)


def about_company(request):
    return render(request, 'main/index3.html')

def mission(request):
    return render(request, 'main/mission.html')

    
def why_this_company(request):
    return render(request, 'main/mission.html')