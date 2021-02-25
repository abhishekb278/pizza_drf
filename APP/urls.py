from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('pizza/',views.MakePizza.as_view(),name="pizza"),
    path('listpizza/',views.ListPizza.as_view(),name="listpizza"),
    path('modpizza/<int:pk>/',views.ModifyPizza.as_view(),name="modpizza")
]