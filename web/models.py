from django.db import models




class Usuario(models.Model):
    RazonS = models.CharField(max_length=150)
    DireccionF = models.CharField(max_length=200)
    CodigoP = models.CharField(max_length=50)
    RFC = models.CharField(max_length=50)
    DireccionE = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=120)
    
    
class Pedidos(models.Model):
    Moneda = models.CharField(max_length=50)
    Solicitante = models.CharField(max_length=120)
    Empresa = models.CharField(max_length=200)
    Direccion = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=100)  
    Cantidad = models.CharField(max_length=100) 
    Detalles = models.CharField(max_length=400)
    
   
    


    
    
