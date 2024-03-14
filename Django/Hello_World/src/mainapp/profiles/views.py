from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Profiles
from .forms import ProfileForm
def admin_con(request):
    profiless = Profiles.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiless': profiless})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profiles, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_con')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profile.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profiles, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_con')
    context = {'item': item}
    return render(request, 'profiles/confirmDelete.html', context)

def confirmed(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_con')
    else:
        return redirect('admin_con')

def createRecord(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_con')
    else:
        print(form.errors)
        form = ProfileForm()
    context = {'form': form}
    return render(request, 'profiles/createRecord.html', context)

