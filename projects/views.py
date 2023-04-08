from django.shortcuts import render
from .forms import ProjectForm
from .models import Project


def projects_list(request):
    all_projects = Project.objects.all()
    context = {
        'all_projects': all_projects
    }
    return render(request, 'projects/projects_list.html', context)


def project_add(request):
    
    form  = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit = False)
            form_instance.author = request.user
            form_instance.save()
            messages.success(request, "New project has been added.")
            return redirect("projects:projects_list")

    context = {
        "form": form
    }
    return render(request, 'projects/project_add.html', context)


def project_details(request, id):
    project = get_object_or_404(Project, id = id)
    context = {
        'project': project
    }
    return render(request, 'projects/project_details.html', context)