from django.views import generic
from taxi.models import TaxiService


class IndexView(generic.ListView):
    template_name = 'taxi/index.html'
    context_object_name = 'services'

    def get_queryset(self):
        return TaxiService.objects.all()


class Detail(generic.DetailView):
    model = TaxiService
    template_name = 'taxi/detail.html'
