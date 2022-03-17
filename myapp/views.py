from django.shortcuts import redirect, render
from .models import Banner, Category, ContactForm, OurWorks, Partner, WorkImages
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    our_works = OurWorks.objects.all().order_by('-created_at')[:10]
    partners = Partner.objects.all().order_by('-created_at')[:4]
    banner = Banner.objects.order_by("-id").all().first()
    ctx = {
        "home":"active",
        "our_works": our_works,
        "partners": partners,
        "banner": banner
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
    
    projects = OurWorks.objects.order_by('-created_at')
    categories = Category.objects.all()
    paginator = Paginator(projects, 6)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)
    ctx = {
        "works":"active",
        "projects": paged_projects,
        "categories": categories,
        'paged_cars': paged_projects,
    }
    return render(request, 'main/works-grid.html',ctx)


def about_company(request):
    ctx = {
         "home":"active",
    }
    return render(request, 'main/index3.html',ctx)

def mission(request):
    ctx = {
         "home":"active",
    }
    return render(request, 'main/mission.html',ctx)

    
def why_this_company(request):
    ctx = {
         "home":"active",
    }
    return render(request, 'main/mission.html',ctx)



def work_details(request,pk):
    project = OurWorks.objects.get(pk=pk)
    images = WorkImages.objects.filter(our_works__id=pk)
    antoher_projects = OurWorks.objects.filter(~Q(pk=project.id),category=project.category)[:4]
    ctx = {
        "works":"active",
        "project": project,
        "images": images,
        "antoher_projects":antoher_projects
    }
    return render(request, 'main/work-details.html',ctx)