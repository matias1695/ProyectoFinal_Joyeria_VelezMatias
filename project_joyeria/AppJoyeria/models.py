from django.db import models
import datetime
# Create your models here.

class Articulo(models.Model):
    idArt=models.CharField(max_length=5)#A****
    nomArt=models.CharField(max_length=30)
    precioArt=models.FloatField()
    material=models.CharField(max_length=10)
    
    def __str__(self) :
        return f"ID: {self.idArt} -- Nombre: {self.nomArt} -- Precio: ${self.precioArt} -- Material: {self.material}"
    
class Cliente(models.Model):
    idCliente=models.CharField(max_length=5)#C****
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    mail=models.EmailField()

    def __str__(self) :
        return f"ID: {self.idCliente} -- Nombre: {self.nombre} -- Apellido ${self.apellido} -- Direccion de Email: {self.mail}"
    
    
class Venta(models.Model):
    TIPOPAGO_CHOICES = [
        ('Efectivo', 'efectivo'),
        ('Tarjeta Db', 'tarjeta db'),
        ('Tarjeta Cr', 'tarjeta cr'),
        ('Transferencia', 'transferencia'),
    ]
    
    idVenta=models.CharField(max_length=5)#V****
    fecha=models.DateField(default=datetime.date.today)
    idCliente=models.CharField(max_length=5)
    idArt=models.CharField(max_length=5)
    cant=models.IntegerField(null=True)
    montoVta=models.FloatField(null=True)
    tipoPago=models.CharField(max_length=15, choices=TIPOPAGO_CHOICES, default='')
    
    def __str__(self) :
        return f"ID: {self.idVenta} -- Id Cliente: {self.idCliente} -- Id Art: ${self.idArt} -- Cantidad: {self.cant} -- Monto Venta: ${self.montoVta} -- Tipo de Pago: {self.tipoPago}"
    


class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('asignado', 'Asignado'),
        ('terminado', 'Terminado'),
    ]

    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='asignado')

    def __str__(self):
        return f"Titulo: {self.titulo} -- Estado: {self.estado}"
