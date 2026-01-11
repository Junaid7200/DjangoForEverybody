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

# Breed Views

class BreedList(LoginRequiredMixin, ListView):
    model = Breed
    template_name = "cats/breed_list.html"
    context_object_name = "breeds"

class CreateBreed(LoginRequiredMixin, CreateView):
    model = Breed
    template_name = "cats/breed_form.html"
    fields = "__all__"
    success_url = reverse_lazy("breed_list")

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    template_name = "cats/breed_form.html"
    fields = "__all__"
    success_url = reverse_lazy("breed_list")

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    template_name = "cats/breed_confirm_delete.html"
    success_url = reverse_lazy("breed_list")