from django.http import JsonResponse
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


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def searchResults(request):
    if is_ajax(request=request):
        res = None
        mobile = request.POST.get('mobile')
        qs = Mobile.objects.filter(modelName__icontains=mobile)
        if len(qs) > 0 and len(mobile) > 0:
            data = []
            for foo in qs:
                item = {
                    'pk' : foo.pk,
                    'brandName': foo.brandName,
                    'modelName': foo.modelName,
                    'color': foo.color,
                    'janCode': foo.janCode,
                    'image': str(foo.image.url)
                }
                data.append(item)
            res = data
        else:
            pass
        return JsonResponse({'data': res})
    return JsonResponse({})


def ajaxSearch(request):
    return render(request, 'mobile/ajaxSearch.html')


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