# from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from base.models import Developer
from pages.forms import DeveloperForm



def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/service.html')


def contact(request):
    return render(request, 'pages/contact.html')


def devcolaborators(request):
    devrs = Developer.objects.all()
    data = {
        'devs': devrs
    }
    return render(request, 'pages/list_devs.html', data)
    



def developer_detail(request, developer_id):
  developer = get_object_or_404(Developer, developer_id=developer_id)
  context = {'developer': developer}
  return render(request, 'pages/devcolabs.html', context)


def developer_add(request):
  if request.method == 'POST':
    form = DeveloperForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('developer_list')  # Redirect to list after creation
  else:
    form = DeveloperForm()
  context = {'form': form}
  return render(request, 'pages/add.html', context)




def developer_edit(request, developer_id):
    developer = get_object_or_404(Developer, developer_id=developer_id)
    if request.method == 'POST':
        form = DeveloperForm(request.POST, instance=developer)  # Pre-populate form with existing data
        if form.is_valid():
            form.save()
            return redirect('developer_detail', developer.developer_id)  # Redirect to detail page after update
    else:
        form = DeveloperForm(instance=developer)  # Create form with existing data
    context = {'form': form, 'developer': developer}
    return render(request, 'pages/edit.html', context)





def developer_delete(request, developer_id):
    if request.method == 'POST':
        developer = get_object_or_404(Developer, developer_id=developer_id)
        developer.delete()
        return redirect('developer_list')  # Redirect to list view after deletion
    else:
        developer = get_object_or_404(Developer, developer_id=developer_id)
        context = {'developer': developer}
        return render(request, 'pages/list_devs.html', context)
    




