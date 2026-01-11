from django.urls import path
from . import views

urlpatterns = [
    # list, edit, and delete a cat
    path("", views.CatList.as_view(), name="cat_list"),
    path("create/", views.CatCreate.as_view(), name="cat_create"),
    path("<int:pk>/update/", views.CatUpdate.as_view(), name="cat_update"),
    path("<int:pk>/delete/", views.CatDelete.as_view(), name="cat_delete"),
    # list, edit, and delete a breed
    path("breeds/", views.BreedList.as_view(), name="breed_list"),
    path("breeds/create/", views.CreateBreed.as_view(), name="breed_create"),
    path("breed/<int:pk>/update", views.BreedUpdate, name="breed_update"),
    path("breed/<int:pk>/delete", views.BreedDelete, name="delete_breed"),
    # BreedUpdate and BreedDelete are functional view practice
]