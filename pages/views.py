from django.shortcuts import render


def index(request):

    context = {

    }
    return render(request, 'pages/index.html', context)


def about_us(request):

    context = {

    }
    return render(request, 'pages/about_us.html', context)


def privacy(request):

    context = {

    }
    return render(request, 'pages/privacy.html', context)


def terms(request):

    context = {

    }
    return render(request, 'pages/terms.html', context)