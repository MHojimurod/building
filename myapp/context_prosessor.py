from myapp.models import OurWorks


def projects(request):
    projects = OurWorks.objects.all()[:10]
    return {"projects":projects}


def day_nights(request):
    print(request.GET.get('day_night'),"day_nights")
    return {}