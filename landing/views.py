from django.shortcuts import render
from .forms import SubscriberForm

def landing(request):
    name = 'Abraha,'
    dateCurent = '14-05-2018'

    form = SubscriberForm(request.POST or None)

    if request.method == 'POST' and form.is.valid():
        print (form)#принтим форму в консоль для проверки
        print (form.cleaned_data)
        data = form.cleaned_data
        print(data.["name"])

        new_form = form.save()
    return render(request, 'landing/landing.html', locals())