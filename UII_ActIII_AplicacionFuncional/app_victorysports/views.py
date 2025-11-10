# app_victorysports/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Proveedor, Producto
from django.db import IntegrityError 

# Función de inicio
def inicio_victorysports(request):
    return render(request, 'inicio.html') 

# ----------------------
# Funciones CRUD Proveedor
# ----------------------

# CREATE: Agregar proveedor
def agregar_proveedor(request):
    if request.method == 'POST':
        try:
            Proveedor.objects.create(
                nombre_empresa=request.POST.get('nombre_empresa'),
                telefono_empresa=request.POST.get('telefono_empresa'),
                email_empresa=request.POST.get('email_empresa'),
                pais_origen=request.POST.get('pais_origen'),
                contacto_principal=request.POST.get('contacto_principal'),
                direccion=request.POST.get('direccion')
            )
            return redirect(reverse('ver_proveedor'))
        except IntegrityError:
            context = {'error_message': 'Ya existe un proveedor con ese nombre de empresa.'}
            return render(request, 'proveedor/agregar_proveedor.html', context)
        except Exception as e:
            context = {'error_message': f'Ocurrió un error: {e}'}
            return render(request, 'proveedor/agregar_proveedor.html', context)
    return render(request, 'proveedor/agregar_proveedor.html')

# READ: Ver proveedores
def ver_proveedor(request):
    proveedores = Proveedor.objects.all().order_by('nombre_empresa')
    context = {'proveedores': proveedores}
    return render(request, 'proveedor/ver_proveedor.html', context)

# UPDATE (Formulario): Obtener proveedor a actualizar
def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    context = {'proveedor': proveedor}
    return render(request, 'proveedor/actualizar_proveedor.html', context)

# UPDATE (Procesamiento): Realizar la actualización
def realizar_actualizacion_proveedor(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('id_proveedor')
        proveedor = get_object_or_404(Proveedor, pk=proveedor_id)

        try:
            proveedor.nombre_empresa = request.POST.get('nombre_empresa')
            proveedor.telefono_empresa = request.POST.get('telefono_empresa')
            proveedor.email_empresa = request.POST.get('email_empresa')
            proveedor.pais_origen = request.POST.get('pais_origen')
            proveedor.contacto_principal = request.POST.get('contacto_principal')
            proveedor.direccion = request.POST.get('direccion')
            
            proveedor.save()
            return redirect(reverse('ver_proveedor'))
        except IntegrityError:
            context = {'proveedor': proveedor, 'error_message': 'Ya existe un proveedor con ese nombre de empresa.'}
            return render(request, 'proveedor/actualizar_proveedor.html', context)
        except Exception as e:
            context = {'proveedor': proveedor, 'error_message': f'Ocurrió un error: {e}'}
            return render(request, 'proveedor/actualizar_proveedor.html', context)
    return redirect(reverse('ver_proveedor'))

# DELETE: Borrar proveedor
def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    
    if request.method == 'POST':
        proveedor.delete()
        return redirect(reverse('ver_proveedor'))
    
    context = {'proveedor': proveedor}
    return render(request, 'proveedor/borrar_proveedor.html', context)


# ----------------------
# Funciones CRUD Producto
# ----------------------

# CREATE: Agregar producto
def agregar_producto(request):
    if request.method == 'POST':
        try:
            Producto.objects.create(
                nombre=request.POST.get('nombre'),
                precio_unitario=request.POST.get('precio_unitario'),
                stock=request.POST.get('stock'),
                marca=request.POST.get('marca'),
                img_url=request.POST.get('img_url'),
                categoria=request.POST.get('categoria'),
                color=request.POST.get('color')
            )
            return redirect(reverse('ver_producto'))
        except Exception as e:
            context = {'error_message': f'Ocurrió un error al guardar: {e}'}
            return render(request, 'producto/agregar_producto.html', context)
    return render(request, 'producto/agregar_producto.html')

# READ: Ver productos
def ver_producto(request):
    productos = Producto.objects.all().order_by('nombre')
    context = {'productos': productos}
    return render(request, 'producto/ver_producto.html', context)

# UPDATE (Formulario): Obtener producto a actualizar
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    context = {'producto': producto}
    return render(request, 'producto/actualizar_producto.html', context)

# UPDATE (Procesamiento): Realizar la actualización
def realizar_actualizacion_producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('id_producto')
        producto = get_object_or_404(Producto, pk=producto_id)

        try:
            producto.nombre = request.POST.get('nombre')
            producto.precio_unitario = request.POST.get('precio_unitario')
            producto.stock = request.POST.get('stock')
            producto.marca = request.POST.get('marca')
            producto.img_url = request.POST.get('img_url')
            producto.categoria = request.POST.get('categoria')
            producto.color = request.POST.get('color')
            
            producto.save()
            return redirect(reverse('ver_producto'))
        except Exception as e:
            context = {'producto': producto, 'error_message': f'Ocurrió un error al actualizar: {e}'}
            return render(request, 'producto/actualizar_producto.html', context)
    return redirect(reverse('ver_producto'))

# DELETE: Borrar producto
def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        producto.delete()
        return redirect(reverse('ver_producto'))
    
    context = {'producto': producto}
    return render(request, 'producto/borrar_producto.html', context)