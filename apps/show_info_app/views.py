from django.shortcuts import render, redirect, 
from django.contrib import messages
from .models import *

def session_showinfo_clear():
    if 'title' in request.session:
        del request.session['title']
    if 'network' in request.session:
        del request.session['network']
    if 'release_date' in request.session:
        del request.session['release_date']
    if 'desc' in request.session:
        del request.session['desc']

def index(request):
    return redirect("/shows/")

def new_show(request):
    context = {}
    return render(request, "show_info_app/edit_show.html", context)

def create_show(request):
    errors = Show.objects.input_vaildator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('shows/create')
    else:
        new_show = Show.objects.create(title=request.POST['show_title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['show_desc'])
        return redirect("/shows/"+str(new_show.id))

def show(request, s_id):
    context = {
        'show': Show.objects.get(id=s_id)
    }
    return render(request, "show_info_app/show_info.html", context)

def edit_show(request, s_id):
    show = Show.objects.get(id=s_id)
    print(show.release_date)
    show_release = Show.objects.get(id=s_id).release_date.strftime("%Y-%m-%d")
    print(show_release)
    context = {
        'show': Show.objects.get(id=s_id),
        'show_release': show_release
    }
    return render(request, "show_info_app/edit_show.html", context)

def delete_show(request, s_id):
    show_to_delete = Show.objects.get(id=s_id)
    show_to_delete.delete()
    return redirect("/shows/")

def all_shows(request):
    context = {
        'shows': Show.objects.all().values()
    }
    return render(request, "show_info_app/all_shows.html", context)

def update_show(request):
    show_to_update = Show.objects.get(id=request.POST['id'])
    show_to_update.title = request.POST['show_title']
    show_to_update.desc = request.POST['show_desc']
    show_to_update.release_date = request.POST['release_date']
    show_to_update.network = request.POST['network']
    print(show_to_update)
    show_to_update.save()
    return redirect("/shows/"+str(request.POST['id']))




# Create your views here.
