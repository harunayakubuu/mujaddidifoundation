from django.shortcuts import render


def donate(request):

    context = {

    }
    return render(request, 'donations/donate.html', context)


def donations(request):

    context = {

    }
    return render(request, 'donations/donations.html', context)


def donors(request):

    context = {

    }
    return render(request, 'donations/donors.html', context)