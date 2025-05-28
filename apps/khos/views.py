from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from .forms import KhoForm
from .models import Kho

# User = get_user_model()


# phòng ban
def kho_list(request):
    khos = Kho.objects.all()
    return render(request, 'khos/kho_list.html', {'khos': khos})

def kho_create(request):
    if request.method == 'POST':
        form = KhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kho_list')
    else:
        form = KhoForm()
    return render(request, 'khos/kho_form.html', {'form': form})

def kho_update(request, pk):
    kho = get_object_or_404(kho, pk=pk)
    if request.method == 'POST':
        form = KhoForm(request.POST, instance=kho)
        if form.is_valid():
            form.save()
            return redirect('kho_list')
    else:
        form = KhoForm(instance=kho)
    return render(request, 'khos/kho_form.html', {'form': form})

def kho_delete(request, pk):
    kho = get_object_or_404(kho, pk=pk)
    if request.method == 'POST':
        kho.delete()
        return redirect('kho_list')
    return render(request, 'khos/kho_confirm_delete.html', {'kho': kho})