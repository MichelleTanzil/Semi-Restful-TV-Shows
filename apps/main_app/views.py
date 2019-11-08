from django.shortcuts import render, redirect
from .models import Show

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
    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['description'])

    return redirect(f"/shows/{new_show.id}")

def show_profile(request, show_id):
  context = {
    'show': Show.objects.get(id=show_id),
  }
  return render(request, 'main_app/show_profile.html', context)

def edit_profile(request, show_id):
    context={
      'show': Show.objects.get(id=show_id),
    }
    return render(request, 'main_app/edit_profile.html', context)

def update_profile(request, show_id):
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.desc = request.POST['description']
    show.save()
    return redirect(f"/shows/{show_id}")

def destroy_profile(reqest, show_id):
    show=Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')