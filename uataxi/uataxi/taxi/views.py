from django.http import Http404
from django.shortcuts import render, get_object_or_404
from taxi.models import TaxiService


def index(request):
    services = TaxiService.objects.all()
    return render(request,
                  'taxi/index.html',
                  {'services': services})


def detail(request, id):
    service = get_object_or_404(TaxiService, pk=id)
    phones = service.phonenumber_set.all()
    return render(request,
                  'taxi/detail.html',
                  {'service': service,
                   'phones': phones})
