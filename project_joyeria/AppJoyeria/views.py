from django.shortcuts import render,redirect
from .models import *
from AppJoyeria.forms import *
from django.db.models import Q #para realizar consultas mas complejas
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
#from django.http import HttpResponse
# Create your views here.
@login_required
def inicio(request):
    return render(request,"AppJoyeria/inicio.html")
@login_required
def articulos(request):
    return render(request,"AppJoyeria/articulos/articulos.html")
@login_required
def clientes(request):
    return render(request, "AppJoyeria/clientes/clientes.html")
@login_required
def ventas(request):
    return render(request, "AppJoyeria/ventas/ventas.html")

@login_required
def tareas(request):
    return render(request, "AppJoyeria/tareas/tareas.html")


#Ventas
class VentasListViews(ListView,LoginRequiredMixin):
    model=Venta
    template_name="AppJoyeria/ventas/leerVentas.html"
    context_object_name = "ventas" 
    paginate_by = 5
    
    def get(self,request,*args, **kagrs):
        return super().get(request,*args,**kagrs)

class VentasDetailViews(DetailView,LoginRequiredMixin):
    model=Venta
    template_name="AppJoyeria/ventas/detalleVentas.html"

class VentasAddViews(CreateView,LoginRequiredMixin):
    model= Venta
    form_class=VentaForm
    template_name= "AppJoyeria/ventas/cargaVentas.html"
    success_url= reverse_lazy('ventas')
    
    
class VentaEditView(UpdateView,LoginRequiredMixin):
    model=Venta
    form_class = VentaForm
    template_name="AppJoyeria/ventas/editarVenta.html"
    success_url= reverse_lazy('leerVentas')
    
    
    
class VentaDeleteV(PermissionRequiredMixin, DeleteView):
    model = Venta
    template_name = "AppJoyeria/ventas/eliminarVenta.html"
    success_url = reverse_lazy('leerVentas')
    permission_required = 'ventas.delete_venta'
    
    def handle_no_permission(self):
        return redirect('leerVentas')

@login_required
def buscarVenta(request):
    if request.method == "POST":
        mi_formulario = BuscarVenta(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            ventas = Venta.objects.filter(tipoPago__icontains=informacion["tipoPago"])
            
            return render(request, "AppJoyeria/ventas/leerVentas.html", {"ventas": ventas})
    else:
        mi_formulario = BuscarVenta()  # Asegúrate de crear una instancia del formulario

    return render(request, "AppJoyeria/ventas/buscarVentas.html", {"mi_formulario": mi_formulario})

#-------------------------------------------------------

#clientes
class ClientesListViews(ListView,LoginRequiredMixin):
    model=Cliente
    template_name="AppJoyeria/clientes/leerClientes.html"
    context_object_name = "clientes" 
    paginate_by = 5
    
    def get(self,request,*args, **kagrs):
        return super().get(request,*args,**kagrs)
    
class ClientesDetailViews(DetailView,LoginRequiredMixin):
    model=Cliente
    template_name="AppJoyeria/clientes/detalleCliente.html"

class ClienteAddViews(CreateView,LoginRequiredMixin):
    model= Cliente
    form_class = ClienteForm
    template_name= "AppJoyeria/clientes/cargaCliente.html"
    success_url= reverse_lazy('clientes')

class ClienteEditView(UpdateView,LoginRequiredMixin):
    model=Cliente
    template_name="AppJoyeria/clientes/editarCliente.html"
    success_url= reverse_lazy('leerClientes')
    form_class=ClienteForm
    
class ClienteDeleteV(PermissionRequiredMixin,DeleteView):
    model=Cliente
    template_name="AppJoyeria/clientes/eliminarCliente.html"
    success_url= reverse_lazy('leerClientes')
    permission_required = 'clientes.delete_cliente'
    
    def handle_no_permission(self):
        return redirect('leerClientes')
    
@login_required   
def buscarCliente(request):
    if request.method == "POST":
        mi_formulario = BuscarClienteForm(request.POST)  # Aquí me llega la información del HTML

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            # Utilizo Q para combinar los filtros de búsqueda
            query = Q()
            if informacion["nombre"]:
                query &= Q(nombre__icontains=informacion["nombre"])
            if informacion["apellido"]:
                query &= Q(apellido__icontains=informacion["apellido"])

            clientes = Cliente.objects.filter(query)

            return render(request, "AppJoyeria/clientes/leerClientes.html", {"clientes": clientes})
    else:
        mi_formulario = BuscarClienteForm()

    return render(request, "AppJoyeria/clientes/buscarCliente.html", {"mi_formulario": mi_formulario})

#-----------------------------------------------------------------
#Articulos
class ArtsListViews(ListView,LoginRequiredMixin):
    model=Articulo
    template_name="AppJoyeria/articulos/leerArticulos.html"
    context_object_name = "articulos" 
    paginate_by = 5
    
    def get(self,request,*args, **kagrs):
        return super().get(request,*args,**kagrs)
    
class ArtDetailViews(DetailView,LoginRequiredMixin):
    model=Articulo
    template_name="AppJoyeria/articulos/detalleArt.html"

class ArtAddViews(CreateView,LoginRequiredMixin):
    model= Articulo
    form_class = ArticuloForm
    template_name= "AppJoyeria/articulos/cargaArt.html"
    success_url= reverse_lazy('articulos')
    
    
class ArtEditView(UpdateView,LoginRequiredMixin):
    model=Articulo
    template_name="AppJoyeria/articulos/editarArt.html"
    success_url= reverse_lazy('leerArticulos')
    form_class = ArticuloForm
    
class ArtDeleteV(PermissionRequiredMixin,DeleteView):
    model=Articulo
    template_name="AppJoyeria/articulos/eliminarArt.html"
    success_url= reverse_lazy('leerArticulos')
    permission_required = 'articulos.delete_articulo'
    
    def handle_no_permission(self):
        return redirect('leerArticulos')
    
@login_required
def buscarArt(request):
    if request.method == "POST":
        mi_formulario = BucarArtForm(request.POST)  # Aquí me llega la información del HTML

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            # Utilizo Q para combinar los filtros de búsqueda
            query = Q()
            if informacion["idArt"]:
                query &= Q(idArt__icontains=informacion["idArt"])
            if informacion["nomArt"]:
                query &= Q(nomArt__icontains=informacion["nomArt"])
            if informacion["material"]:
                query &= Q(material__icontains=informacion["material"])

            articulos = Articulo.objects.filter(query)

            return render(request, "AppJoyeria/articulos/leerArticulos.html", {"articulos": articulos})
    else:
        mi_formulario = BucarArtForm()

    return render(request, "AppJoyeria/articulos/buscarArt.html", {"mi_formulario": mi_formulario})
#-----------------------------------------------------------------------------------

#Tareas
class TareaListViews(ListView,LoginRequiredMixin):
    model=Tarea
    template_name="AppJoyeria/tareas/leerTareas.html"
    context_object_name = "tareas" 
    paginate_by = 5
    
    def get(self,request,*args, **kagrs):
        return super().get(request,*args,**kagrs)
    
    def get_queryset(self):
        return Tarea.objects.order_by('fecha')
    
class TareaDetailViews(DetailView,LoginRequiredMixin):
    model=Tarea
    template_name="AppJoyeria/tareas/detalleTarea.html"

class TareaAddViews(CreateView, LoginRequiredMixin):
    model = Tarea
    template_name = "AppJoyeria/tareas/cargaTarea.html"
    form_class = TareaForm  #uso en vez de fields
    success_url = reverse_lazy('tareas')

class TareaEditView(UpdateView,LoginRequiredMixin):
    model=Tarea
    form_class = TareaEditForm
    template_name="AppJoyeria/tareas/editarTarea.html"
    success_url= reverse_lazy('leerTareas')
    
class TareaDeleteV(PermissionRequiredMixin,DeleteView):
    model=Tarea
    template_name="AppJoyeria/tareas/eliminarTarea.html"
    success_url= reverse_lazy('leerTareas')
    permission_required = 'tareas.delete_tarea'
    
    def handle_no_permission(self):
        return redirect('leerTareas')   
    
@login_required
def buscarTarea(request):
    if request.method == "POST":
        mi_formulario = BuscarTarea(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            tareas = Tarea.objects.filter(estado__icontains=informacion["estado"])
            
            return render(request, "AppJoyeria/tareas/leerTareas.html", {"tareas": tareas})
    else:
        mi_formulario = BuscarTarea()  # Asegúra de crear una instancia del formulario

    return render(request, "AppJoyeria/tareas/buscarTarea.html", {"mi_formulario": mi_formulario})