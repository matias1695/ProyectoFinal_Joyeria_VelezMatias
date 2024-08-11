"""
URL configuration for project_joyeria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
]
#Ventas
urlpatterns += [
    path('ventas',views.ventas,name="ventas"),
    path('ventas/nuevo',views.VentasAddViews.as_view(),name="cargaVentas"),
    path('leerVentas/',views.VentasListViews.as_view(),name="leerVentas"), 
    path('ventas/<pk>',views.VentasDetailViews.as_view(),name="detalleVentas"),
    path('ventas/<pk>/editar',views.VentaEditView.as_view(),name='editarVentas'),
    path('ventas/<pk>/eliminar',views.VentaDeleteV.as_view(),name='eliminarVentas'),
    path('buscarVenta/',views.buscarVenta,name='buscarVentas'),
]

#Clientes
urlpatterns += [
    path('clientes',views.clientes,name="clientes"),
    path('clientes/nuevo',views.ClienteAddViews.as_view(),name="cargaCliente"),
    path('leerClientes/',views.ClientesListViews.as_view(),name="leerClientes"),
    path('clientes/<pk>',views.ClientesDetailViews.as_view(),name="detalleClientes"),
    path('clientes/<pk>/editar',views.ClienteEditView.as_view(),name='editarCliente'),
    path('clientes/<pk>/eliminar',views.ClienteDeleteV.as_view(),name='eliminarCliente'),
    path('buscarCliente/',views.buscarCliente,name='buscarCliente'),
]

#Articulos
urlpatterns += [
    path('articulos',views.articulos,name="articulos"),
    path('articulos/nuevo',views.ArtAddViews.as_view(),name="cargaArticulo"),
    path('leerArticulos/',views.ArtsListViews.as_view(),name="leerArticulos"),
    path('articulos/<pk>',views.ArtDetailViews.as_view(),name="detalleArt"),
    path('articulos/<pk>/editar',views.ArtEditView.as_view(),name='editarArt'),
    path('articulos/<pk>/eliminar',views.ArtDeleteV.as_view(),name='eliminarArt'),
    path('buscarArt/', views.buscarArt, name="buscarArticulos"),
]

#Tareas
urlpatterns += [
    path('tareas',views.tareas,name='tareas'),
    path('leerTareas/',views.TareaListViews.as_view(),name='leerTareas'),
    path('tareas/nuevo',views.TareaAddViews.as_view(),name='cargaTarea'),
    path('tareas/<pk>',views.TareaDetailViews.as_view(),name='detalleTarea'),
    path('tareas/<pk>/editar',views.TareaEditView.as_view(),name='editarTarea'),
    path('tareas/<pk>/eliminar',views.TareaDeleteV.as_view(),name='eliminarTarea'),
    path('buscarTarea/',views.buscarTarea,name='buscarTarea'),

]