from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed

# Create your views here.

class CatList(LoginRequiredMixin, ListView):
    model = Cat
    template_name = "cats/cat_list.html"
    context_object_name = "cats"

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    template_name = "cats/cat_form.html"
    fields = "__all__"
    success_url = reverse_lazy("cat_list")

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    template_name = "cats/cat_form.html"
    fields = "__all__"
    success_url = reverse_lazy("cat_list")

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    template_name = "cats/cat_confirm_delete.html"
    success_url = reverse_lazy("cat_list")

