from django import forms   
from .models import Tarea,Articulo,Cliente,Venta

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['idArt', 'nomArt', 'precioArt', 'material']
        labels = {
            'idArt': 'ID del Artículo',
            'nomArt': 'Descripción',
            'precioArt': 'Precio',
            'material': 'Material',
        }
        widgets = {
            'idArt': forms.TextInput(attrs={'class': 'form-control'}),
            'nomArt': forms.TextInput(attrs={'class': 'form-control'}),
            'precioArt': forms.NumberInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
class BucarArtForm(forms.Form):
    idArt=forms.CharField()
    nomArt=forms.CharField()
    material=forms.CharField()
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['idCliente', 'nombre', 'apellido', 'mail']
        labels = {
            'idCliente': 'ID-Cliente',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'mail': 'Mail',
        }
        widgets = {
            'idCliente': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.NumberInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BuscarClienteForm(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['idVenta', 'fecha', 'idCliente', 'idArt', 'cant', 'montoVta', 'tipoPago']
        labels = {
            'idVenta': 'ID de la Venta',
            'fecha': 'Fecha',
            'idCliente': 'ID del Cliente',
            'idArt': 'ID del Artículo',
            'cant': 'Cantidad',
            'montoVta': 'Monto de la Venta',
            'tipoPago': 'Tipo de Pago',
        }
        widgets = {
            'idVenta': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'idCliente': forms.TextInput(attrs={'class': 'form-control'}),
            'idArt': forms.TextInput(attrs={'class': 'form-control'}),
            'cant': forms.NumberInput(attrs={'class': 'form-control'}),
            'montoVta': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tipoPago': forms.Select(attrs={'class': 'form-control'}),
        }
    
class BuscarVenta(forms.Form):
    tipoPago=forms.CharField()


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha', 'estado']
        widgets = {
            'fecha': forms.SelectDateWidget(),
            'descripcion': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].initial = 'Asignado'  # Valor predeterminado para 'estado'
        

class TareaEditForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={'readonly': 'readonly'}),
            'descripcion': forms.Textarea(attrs={'readonly': 'readonly'}),
            'fecha': forms.DateInput(attrs={'readonly': 'readonly'}),
            'estado': forms.Select()#con esto genera menu desplegable
        }
    
class BuscarTarea(forms.Form):
    estado=forms.CharField()