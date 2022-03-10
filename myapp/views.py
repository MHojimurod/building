from django.shortcuts import redirect, render
from .models import Category, ContactForm, OurWorks, Partner, WorkImages
from django.contrib import messages

# Create your views here.
def home(request):
    our_works = OurWorks.objects.all().order_by('-created_at')[:10]
    partners = Partner.objects.all().order_by('-created_at')[:4]
    ctx = {
        "home":"active",
        "our_works": our_works,
        "partners": partners,
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
    projects = OurWorks.objects.all()
    categories = Category.objects.all()
    ctx = {
        "works":"active",
        "projects": projects,
        "categories": categories,
    }
    return render(request, 'main/works-grid.html',ctx)


def about_company(request):
    return render(request, 'main/index3.html')

def mission(request):
    return render(request, 'main/mission.html')

    
def why_this_company(request):
    return render(request, 'main/mission.html')



def work_details(request,pk):
    project = OurWorks.objects.get(pk=pk)
    images = WorkImages.objects.filter(our_works__id=pk)
    ctx = {
        "project": project,
        "images": images
    }
    return render(request, 'main/work-details.html',ctx)