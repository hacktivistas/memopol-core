
import datetime
import urllib
from django.views.generic import DetailView, ListView
from memopol.es.parliament.models import ESParlamentary

from os.path import join
from django.conf import settings

from memopol.base.utils import check_dir, send_file, get_content_cache

ES_IMAGE_URL = u"http://www.congreso.es/wc/htdocs/web/img/diputados/%s_10.jpg"

class ESParlamentaryView(DetailView):
    queryset=ESParlamentary.objects.all()
    context_object_name="esparlamentary"
    #model = ESParlamentary

    def get_context_data(self, *args, **kwargs):
        context = super(ESParlamentaryView, self).get_context_data(**kwargs)
        context['now'] = datetime.date.today()
        #context['mep'].delegationroles = context['mep'].delegationrole_set.all().select_related('delegation')
        #context['mep'].committeeroles = context['mep'].committeerole_set.all().select_related('committee')
        #context['mep'].opinionreps = context['mep'].opinionrep_set.all().select_related('opinion')
        #context['mep'].scores = context['mep'].score_set.all().select_related('proposal')
        return context


class ESPList(ListView):
    active=True
    context_object_name="esparlamentary"
    score_listing=False
    order_by='last_name'

    def get_queryset(self):
        if not self.queryset:
            return ESParlamentary.objects.order_by(self.order_by)
#            return ESParlamentary.objects.filter(active=self.active).order_by(self.order_by)
        return self.queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ESPList, self).get_context_data(**kwargs)
        context['score_listing'] = self.score_listing
        context['active'] = self.active
        return context

    def render_to_response(self, context, **response_kwargs):
#        if 'csv' in self.request.GET:
#            return render_to_csv(self, context, **response_kwargs)
        return super(ESPList, self).render_to_response(context, **response_kwargs)

def get_esp_picture(request, ep_id):
    filename = join(settings.MEDIA_DIRECTORY, 'img', 'esparlamentary', u"%s.jpg" % ep_id)
    cache = get_content_cache(request, filename, 'image/jpeg')
    if cache:
        return cache
    check_dir(filename)
    urllib.urlretrieve(ES_IMAGE_URL % ep_id, filename)
    return send_file(request, filename, content_type='image/jpeg')
