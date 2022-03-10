from myapp.models import OurWorks


def projects(request):
    projects = OurWorks.objects.all()[:10]
    return {"projects":projects}