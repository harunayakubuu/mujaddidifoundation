from django.shortcuts import render


def index(request):

    context = {

    }
    return render(request, 'pages/index.html', context)


def about_us(request):

    context = {

    }
    return render(request, 'pages/about-us.html', context)