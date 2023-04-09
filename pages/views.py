from django.shortcuts import render, get_object_or_404
from blog.models import Post
from .models import FoundationCommittee


def index(request):
    blog_recent = Post.objects.order_by('-created_at').filter(active = True)[:3]
    context = {
        'blog_recent': blog_recent
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


def team(request):
    team = FoundationCommittee.objects.filter(active = True)
    context = {
        'team': team
    }
    return render(request, 'pages/team.html', context)


def team_member(request, id):
    team_member = get_object_or_404(FoundationCommittee, id = id)
    context = {
        'team_member': team_member
    }
    return render(request, 'pages/team_member.html', context)