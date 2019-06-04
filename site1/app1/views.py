from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
# Create your views here.


def hello(request):
    print(request.POST)
    datos = [1, 2, 3]
    nombre = request.GET['nombre']

    return render(request, "hello.html", {'datos': datos, 'nombre': nombre})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/hello/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'forms.html', {'form': form})