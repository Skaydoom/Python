from django.shortcuts import render
from .forms import SubsForm

def landing(request):
    name='Skaydoom'
    current_day="13.11.2017"
    form=SubsForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form=form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    return render(request, 'landing/home.html', locals())

