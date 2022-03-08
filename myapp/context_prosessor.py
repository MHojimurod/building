from myapp.models import OurWorks


def projects(request):
    projects = OurWorks.objects.all()
    return {"projects":projects}