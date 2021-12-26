from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, DeleteView
# Create your views here.


class Mobiles(ListView):
    context_object_name = 'mobiles'
    model = Mobile
    template_name = 'mobile/mobileList.html'


class MobileDetails(DetailView):
    context_object_name = 'mobile'
    model = Mobile
    template_name = 'mobile/detailsInfo.html'


class AddMobile(CreateView):
    fields = '__all__'
    model = Mobile
    template_name = 'mobile/addMobile.html'


def DeleteMobile(request, pk):
    mobile = Mobile.objects.get(pk=pk)
    mobile.delete()
    return redirect('/')