from django.db import models

class AnimalTienda(models.Model):
    nombre_animal = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    estado_salud = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    chip_identificacion = models.CharField(max_length=50)
    vacunas_aplicadas = models.TextField()

    def __str__(self):
        return f"{self.nombre_animal} ({self.especie})"


class CategoriaMascota(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion_categoria = models.TextField()
    es_comida = models.BooleanField(default=False)
    es_juguete = models.BooleanField(default=False)
    aplica_para_especie = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria


class Proveedor(models.Model):  # No estaba en tu tabla, pero se requiere para FK
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class ProductoMascota(models.Model):
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(CategoriaMascota, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    para_especie = models.CharField(max_length=50)
    tamano_animal = models.CharField(max_length=50)
    marca = models.CharField(max_length=100)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre_producto


class ClienteMascota(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateField()
    num_mascotas = models.IntegerField()
    tipo_mascota_preferido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class EmpleadoTiendaMascota(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    dni = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    turno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class VentaTiendaMascota(models.Model):
    fecha_venta = models.DateTimeField()
    cliente = models.ForeignKey(ClienteMascota, on_delete=models.CASCADE)
    empleado = models.ForeignKey(EmpleadoTiendaMascota, on_delete=models.CASCADE)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    descuento_aplicado = models.DecimalField(max_digits=5, decimal_places=2)
    numero_ticket = models.CharField(max_length=50)
    estado_venta = models.CharField(max_length=50)

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta}"


class DetalleVentaTiendaMascota(models.Model):
    venta = models.ForeignKey(VentaTiendaMascota, on_delete=models.CASCADE)
    producto = models.ForeignKey(ProductoMascota, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField()
    precio_unitario_venta = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva_aplicado = models.DecimalField(max_digits=5, decimal_places=2)
    animal_vendido = models.ForeignKey(AnimalTienda, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Detalle Venta #{self.id}"
