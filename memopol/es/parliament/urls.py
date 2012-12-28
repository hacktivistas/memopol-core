from django.conf.urls.defaults import patterns, url, include

from views import ESParlamentaryView, ESPList

urlpatterns = patterns('memopol.es.parliament.views',
    url(r'^deputy/(?P<pk>\w+)/$', ESParlamentaryView.as_view(), name='mep'),
    url(r'^deputy/(?P<pk>\w+)/contact$', ESParlamentaryView.as_view(template_name="parliament/mep_contact.html"), name='esp_contact'),

    url(r'^names/$', ESPList.as_view(), name='index_names'),

)

urlpatterns += patterns('memopol.es.parliament.views',
    url(r'^deputy/(?P<ep_id>[0-9]+)/picture.jpg$', 'get_esp_picture',
        name='esp-picture'),
)
