from django.shortcuts import render

# Create your views here.
from .models import Marca, Producto, Cliente, Venta, DetalleVenta
from datetime import datetime

def insertar_datos_iniciales(request):
    if request.method == 'POST':
        # Verificar y agregar marcas
        if not Marca.objects.filter(nombre='Marca 1').exists():
            marcas = [
                Marca(nombre='Marca 1', descripcion='Descripción 1', estado=True),
                Marca(nombre='Marca 2', descripcion='Descripción 2', estado=True),
            ]
            Marca.objects.bulk_create(marcas)

        # Verificar y agregar productos
        marca = Marca.objects.filter(nombre='Marca 1').first()
        if marca and not Producto.objects.filter(nombre='Producto 1').exists():
            productos = [
                Producto(nombre='Producto 1', descripcion='Producto de prueba 1', precio_unitario=10.0, stock_disponible=100, estado=True, marca=marca),
                Producto(nombre='Producto 2', descripcion='Producto de prueba 2', precio_unitario=20.0, stock_disponible=200, estado=True, marca=marca),
            ]
            Producto.objects.bulk_create(productos)

        # Verificar y agregar clientes
        if not Cliente.objects.filter(nombre='Cliente 1').exists():
            clientes = [
                Cliente(nombre='Cliente 1', direccion='Dirección 1', email='cliente1@example.com', telefono='1234567890', estado=True),
                Cliente(nombre='Cliente 2', direccion='Dirección 2', email='cliente2@example.com', telefono='0987654321', estado=True),
            ]
            Cliente.objects.bulk_create(clientes)

        # Verificar y agregar ventas
        cliente = Cliente.objects.filter(nombre='Cliente 1').first()
        if cliente and not Venta.objects.filter(numero='V001').exists():
            ventas = [
                Venta(numero='V001', fecha=datetime.now(), total=100.0, estado='completada', cliente=cliente),
                Venta(numero='V002', fecha=datetime.now(), total=200.0, estado='completada', cliente=cliente),
            ]
            Venta.objects.bulk_create(ventas)

        # Verificar y agregar detalles de ventas
        venta = Venta.objects.filter(numero='V001').first()
        producto = Producto.objects.filter(nombre='Producto 1').first()
        if venta and producto and not DetalleVenta.objects.filter(venta=venta, producto=producto).exists():
            for i in range(10):
                DetalleVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad=5,
                    precio_unitario=producto.precio_unitario,
                    subtotal=producto.precio_unitario * 5
                )

        return render(request, 'app/datos_insertados.html')
    else:
        return render(request, 'app/insertar_datos.html')

def ver_datos(request):
    # Obtener los datos de cada modelo
    marcas = Marca.objects.all()
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    ventas = Venta.objects.all()
    detalles_ventas = DetalleVenta.objects.all()

    # Pasar los datos al template
    context = {
        'marcas': marcas,
        'productos': productos,
        'clientes': clientes,
        'ventas': ventas,
        'detalles_ventas': detalles_ventas,
    }
    return render(request, 'app/ver_datos.html', context)