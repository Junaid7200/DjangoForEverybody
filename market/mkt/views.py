from . import models

from mkt.owner import OwnerCreateView, OwnerDeleteView, OwnerDetailView, OwnerListView, OwnerUpdateView

# Create your views here.
class AdListView(OwnerListView):
    model = models.Ad
    template_name = 'mkt/ad_list.html'
class AdDetailView(OwnerDetailView):
    model = models.Ad
    template_name = 'mkt/ad_detail.html'
class AdCreateView(OwnerCreateView):
    model = models.Ad
    fields = ['title', 'price', 'text']
    template_name = 'mkt/ad_form.html'
class AdUpdateView(OwnerUpdateView):
    model = models.Ad
    fields = ['title', 'price', 'text']
    template_name = 'mkt/ad_form.html'
class AdDeleteView(OwnerDeleteView):
    model = models.Ad
    template_name = 'mkt/ad_confirm_delete.html'