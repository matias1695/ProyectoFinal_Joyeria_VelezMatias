from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EditarUsuario(forms.ModelForm):
    email=forms.EmailField(label="Ingrese Su Direccion De Correo Electronico")
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput,required=False)
    password2=forms.CharField(label='Repita la Contraseña Ingresada',widget=forms.PasswordInput,required=False)
    nombre= forms.CharField(required=False)
    apellido=forms.CharField(required=False)
    imagen = forms.ImageField(required=False)
    
    
    class Meta:
        model = User
        fields = ['email', 'nombre', 'apellido', 'password1', 'password2']
        

class RegistroUsuario(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', required=True)  # Cambié 'usuario' a 'username'
    email = forms.EmailField(label='Correo Electrónico', required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Repetir Contraseña',
        }
        help_texts = {k: "" for k in fields}
