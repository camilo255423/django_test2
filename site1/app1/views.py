from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm
# Create your views here.


def index(request):
    return HttpResponse("hello")
