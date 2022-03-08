from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {
        "home":"active"
    }
    return render(request, 'main/index.html',ctx)


def contact(request):
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