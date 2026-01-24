from . import models
from mkt.forms import CreateForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy, reverse
from mkt.owner import OwnerDeleteView, OwnerDetailView, OwnerListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from django.db.models import Q

# Create your views here.
class AdListView(OwnerListView):
    model = models.Ad
    template_name = 'mkt/ad_list.html'
    
    def get(self, request):
        strval = request.GET.get('search', False)
        if strval:
            ad_list = models.Ad.objects.filter(
                Q(title__icontains=strval) | Q(text__icontains=strval) | Q(tags__name__icontains=strval)
            ).distinct()
        else:
            ad_list = models.Ad.objects.all()            
        favorites = list()
        if request.user.is_authenticated:
            rows = request.user.ads_favorite.values('id')
            favorites = [row['id'] for row in rows]
        ctx = {'ad_list': ad_list, 'favorites': favorites}
        return render(request, self.template_name, ctx)
    # context_object_name is not defined here so it will be <modelname>_list by default.
    # in the same way, the user object that we will be using in the templates, that is also passed to the templates by default, no need to do anything

class AdDetailView(OwnerDetailView):
    model = models.Ad
    fields = ['title', 'price', 'text']
    template_name = 'mkt/ad_detail.html'

    def get(self, request, pk=None):
        ad = get_object_or_404(models.Ad, id=pk)
        comments = models.Comment.objects.filter(ad=ad).order_by('-updatedAt')
        comment_form = CommentForm()
        ctx = {'ad': ad, 'comments': comments, 'comment_form': comment_form}
        return render(request, self.template_name, ctx)

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
        form.save_m2m()
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
        form.save_m2m()
        return redirect(self.success_url)
class AdDeleteView(OwnerDeleteView):
    model = models.Ad
    template_name = 'mkt/ad_confirm_delete.html'



class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(models.Ad, id=pk)
        form = CommentForm(request.POST)

        if not form.is_valid():
            comments = models.Comment.objects.filter(ad=ad).order_by('-updatedAt')
            ctx = {'ad': ad, 'comments': comments, 'comment_form': form}
            return render(request, 'mkt/ad_detail.html', ctx)

        comment = models.Comment(
            text=form.cleaned_data['comment'],
            owner=request.user,
            ad=ad,
        )
        comment.save()
        return redirect(reverse('mkt:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = models.Comment
    template_name = 'mkt/comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('mkt:ad_detail', args=[self.object.ad_id])

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteToggle(LoginRequiredMixin, View):
    def post(sefl, request, pk):
        ad = get_object_or_404(models.Ad, id=pk)
        fav= models.Favorite(ad=ad, owner=request.user)
        try:
            fav.save()
            return HttpResponse()
        except IntegrityError:
            models.Favorite.objects.filter(ad=ad, owner=request.user).delete()
            return HttpResponse()

def stream_file(request, pk):
    pic = get_object_or_404(models.Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response