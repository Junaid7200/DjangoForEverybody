from . import models
from mkt.forms import CreateForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from mkt.owner import OwnerDeleteView, OwnerDetailView, OwnerListView

# Create your views here.
class AdListView(OwnerListView):
    model = models.Ad
    template_name = 'mkt/ad_list.html'
    fields = ['title', 'price', 'text']
    # context_object_name is not defined here so it will be <modelname>_list by default.
    # in the same way, the user object that we will be using in the templates, that is also passed to the templates by default, no need to do anything
class AdDetailView(OwnerDetailView):
    model = models.Ad
    fields = ['title', 'price', 'text']
    template_name = 'mkt/ad_detail.html'
class AdCreateView(LoginRequiredMixin, View):
    template_name = 'mkt/ad_form.html'
    success_url = reverse_lazy('mkt:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        return redirect(self.success_url)
class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'mkt/ad_form.html'
    success_url = reverse_lazy('mkt:all')

    def get(self, request, pk):
        ad = get_object_or_404(models.Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        ad = get_object_or_404(models.Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        ad = form.save(commit=False)
        ad.save()
        return redirect(self.success_url)
class AdDeleteView(OwnerDeleteView):
    model = models.Ad
    template_name = 'mkt/ad_confirm_delete.html'

def stream_file(request, pk):
    pic = get_object_or_404(models.Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response