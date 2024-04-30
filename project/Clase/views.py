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
            return render(request, 'core/error.html', {'message': 'El nombre y la edad del vendedor son obligatorios'})
    else:
        return render(request, 'core/base.html')

def agregar_pedido(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        producto_id = request.POST.get('productos')
        vendedor_id = request.POST.get('vendedores')
        cliente_id = request.POST.get('clientes')

        pedido = Pedido.objects.create(
            codigo=codigo,
            producto=Producto.objects.get(id=producto_id),
            vendedor=Vendedor.objects.get(id=vendedor_id),
            cliente=Cliente.objects.get(id=cliente_id)
        )

        return redirect('core:home')
    else:
        productos = Producto.objects.all()
        vendedores = Vendedor.objects.all()
        clientes = Cliente.objects.all()

        return render(request, 'core/agregar_pedido.html', {'productos': productos, 'vendedores': vendedores, 'clientes': clientes})




