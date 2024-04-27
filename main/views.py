from django.shortcuts import render

from . import models



def index(request):
    banner = models.Banner.objects.last()
    result = models.Result.objects.all()
    teams = models.Team.objects.all()
    context = {
        'banner' : banner,
        'result' : result,
        'teams' : teams,
    }
    return render(request,'index.html',context )


def service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'Kayıt.html', context)



def blog(request):
    blogs = models.Blog.objects.all()
    context = {
        'blogs' : blogs
    }

    return render(request, 'blog.html', context)


def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name = request.POST['name'],
                phone = request.POST['phone'],
                email = request.POST['email'],
                body = request.POST['body']
            )
        except:
            ...
    return render(request, 'İletişim.html')