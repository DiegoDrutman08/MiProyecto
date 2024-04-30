from django.shortcuts import render, redirect
from .models import Producto, Cliente, Vendedor, Pedido

def home(request):
    return render(request, "core/base.html")

def agregar_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST.get('producto')
        Producto.objects.create(nombre=nombre_producto)
        return redirect('core:home')
    else:
        return render(request, 'core/base.html')

def agregar_cliente(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('cliente')
        Cliente.objects.create(nombre=nombre_cliente)
        return redirect('core:home')
    else:
        return render(request, 'core/base.html')

def agregar_vendedor(request):
    if request.method == 'POST':
        nombre_vendedor = request.POST.get('vendedor')
        edad_vendedor = request.POST.get('edad')
        if nombre_vendedor and edad_vendedor:
            Vendedor.objects.create(nombre=nombre_vendedor, edad=edad_vendedor)
            return redirect('core:home')
        else:
            return render(request, 'core/base.html', {'message': 'El nombre y la edad del vendedor son obligatorios'})
    else:
        return render(request, 'core/base.html')

def agregar_pedido(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        producto_id = request.POST.get('productos')
        vendedor_id = request.POST.get('vendedores')
        cliente_id = request.POST.get('clientes')
        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            producto = None
        try:
            vendedor = Vendedor.objects.get(id=vendedor_id)
        except Vendedor.DoesNotExist:
            vendedor = None
        try:
            cliente = Cliente.objects.get(id=cliente_id)
        except Cliente.DoesNotExist:
            cliente = None

        if producto and vendedor and cliente:
            pedido = Pedido.objects.create(codigo=codigo, producto=producto, vendedor=vendedor, cliente=cliente)
            return redirect('Clase:agregar_pedido')
        else:
            error_message = "Uno o más objetos no existen"
            productos = Producto.objects.all()
            vendedores = Vendedor.objects.all()
            clientes = Cliente.objects.all()
            return render(request, 'core/agregar_pedido.html', {'error_message': error_message, 'productos': productos, 'vendedores': vendedores, 'clientes': clientes})
    else:
        productos = Producto.objects.all()
        vendedores = Vendedor.objects.all()
        clientes = Cliente.objects.all()
        return render(request, 'core/agregar_pedido.html', {'productos': productos, 'vendedores': vendedores, 'clientes': clientes})
