from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from medical.forms import MedicalForm
from medical.models import MedicalStore


@login_required
def medical_view(request):
    query = request.GET.get("q", "")
    if query:
        list_data = MedicalStore.objects.filter(name__icontains=query)
    else:
        list_data = MedicalStore.objects.all()
    context = {
        "list": list_data,
    }
    return render(request, "medical/store.html", context)


def add_medicine(request):
    if request.method == "POST":
        form = MedicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical')
    else:
        form = MedicalForm()
    context = {'form': form}
    return render(request, 'medical/add_medicine.html', context)


def update_view(request, pk):
    if request.method == "POST":
        update = MedicalStore.objects.get(pk=pk)
        form = MedicalForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('medical')
    else:
        update = MedicalStore.objects.get(pk=pk)
        form = MedicalForm(instance=update)

    context = {
        'form': form
    }
    return render(request, 'medical/update.html', context)


def delete_medicine(request, pk):
    dl = MedicalStore.objects.get(pk=pk)
    dl.delete()
    return redirect('medical')


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
