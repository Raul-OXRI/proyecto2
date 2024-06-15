from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.producto, name='products'),
    path ('crudproductos/', views.productocrud, name='crudproductos'),
    path ('downproducto/<int:producto_id>/', views.eliminar_producto, name='downproducto'),
    path ('viewproducto/', views.viewproducto, name='viewproducto'),
    
]
