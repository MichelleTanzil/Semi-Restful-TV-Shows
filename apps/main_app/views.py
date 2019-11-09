from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages


def home_page(request):
    return redirect('/shows')


def index(request):
    context = {
        'all_shows': Show.objects.all(),
    }
    return render(request, 'main_app/index.html', context)


def new(request):
    return render(request, 'main_app/new_show.html')


def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, values in errors.items():
            messages.error(request, values)
        return redirect('/shows/new')
    else:
        new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'],
                                       release_date=request.POST['release_date'], desc=request.POST['description'])
        messages.success(request, "New show successfully updated")
        return redirect(f"/shows/{new_show.id}")


def show_profile(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id),
    }
    return render(request, 'main_app/show_profile.html', context)


def edit_profile(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id),
    }
    return render(request, 'main_app/edit_profile.html', context)


def update_profile(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, values in errors.items():
            messages.error(request, values)
        return redirect(f"/shows/{show_id}/edit")
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['description']
        show.save()
        return redirect(f"/shows/{show_id}")


def destroy_profile(reqest, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')
