from django.conf.urls.defaults import patterns, url
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from votes.models import Proposal, Vote
from reps.models import Representative

def proposal_rep(request, proposal_id, mep_id):
    representative = get_object_or_404(Representative, id=mep_id)
    proposal = get_object_or_404(Proposal, id=proposal_id)
    votes = [Vote.objects.get(representative=representative, recommendation=r) for r in proposal.recommendation_set.all()]
    context = {'representative': representative, 'proposal': proposal, 'votes': votes}
    return render_to_response('votes/per_rep.html', context, context_instance=RequestContext(request))

urlpatterns = patterns('',
    url(r'^$', list_detail.object_list, {'queryset': Proposal.objects.all()}, name='index'),
    url(r'^(?P<proposal_id>[a-zA-Z/-_]+)/(?P<mep_id>[a-zA-Z-_]+)/$', proposal_rep, name='rep'),
    url(r'^(?P<object_id>[a-zA-Z/-_]+)/$', list_detail.object_detail, {'queryset': Proposal.objects.all(), 'template_object_name': 'vote'}, name='detail'),
)
