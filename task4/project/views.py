from django.shortcuts import redirect, render
from .models import Profile

def index(request):
    profile = Profile.objects.all()
    return render(request, '', {'profile':profile})

def create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        profile_obj = Profile.objects.create(first_name=first_name, last_name=last_name,birth_date=birth_date)
        return redirect('')
    return render(request, '')

def update(request, id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        profile_update = Profile.objects.get(id=id)
        profile_update.first_name = first_name
        profile_update.last_name = last_name
        profile_update.birth_date = birth_date
        profile_update.save()
        return redirect('')
    return render(request, '')

def delete(request, id):
    if request.method == 'POST':
        profile_obj = Profile.objects.get(id=id)
        profile_obj.delete()
        return redirect('')
    return render(request, '')