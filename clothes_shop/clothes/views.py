from django.shortcuts import render,redirect
from .models import Cloth
from django.contrib.auth.decorators import login_required
from . import forms


def show_clothes(request):
    clothes = Cloth.objects.all()
    return render(request, 'man/main_clothes.html', {'clothes' : clothes})

def show_cloth_item(request, slug):
    cloth_item = Cloth.objects.get(slug=slug)
    return render(request, 'general/cloth_item.html', {'cloth' : cloth_item})

@login_required(login_url="/users/login/")
def add_new_cloth(request):
    if request.method == 'POST':
        form = forms.AddCloth(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clothes:page')
            
    else:
        form = forms.AddCloth()
    return render(request, 'general/new_cloth.html', {'form' : form})