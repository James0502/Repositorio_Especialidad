import json
import pandas as pd
import xlwt
#nuevas importaciones 30-05-2022
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from registration.models import Profile

#fin nuevas importaciones 30-05-2022

from django.db.models import Count, Avg, Q
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import (
	api_view, authentication_classes, permission_classes)
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from gestioncliente.models import Cliente
from .forms import ClienteForm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import styles
from reportlab.lib.styles import ParagraphStyle



#CLIENTE
@login_required
def clientes_main(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'gestioncliente/clientes_main.html'
    return render(request,template_name,{'profile':profile})

@login_required
def agregar_cliente(request):
    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'cliente creado!')
    return render(request, 'gestioncliente/agregar_cliente.html',data)

@login_required
def listar_cliente(request):
     clientes = Cliente.objects.all()
     data={
         'clientes': clientes
     }
     return render(request, 'gestioncliente/listar_cliente.html',data)
@login_required
def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    data ={
        'form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST,instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_cliente")
    messages.add_message(request, messages.INFO, 'cliente actualizado!')
    return render(request, 'gestioncliente/modificar_cliente.html',data)
@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.add_message(request, messages.INFO, 'cliente eliminado!')
    return redirect(to="listar_cliente")

@login_required
def generar_reporte_clientes(request):
    # Obtener los datos de clientes desde tu modelo
    clientes = Cliente.objects.all()

    # Crear el objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_clientes.pdf"'

    # Crear el objeto PDF utilizando el objeto response como "archivo" donde escribir el PDF
    document = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Estilos para la tabla y el texto
    styles = getSampleStyleSheet()
    style_table = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#CCCCCC'),
        ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), '#EEEEEE'),
    ])
    style_paragraph = ParagraphStyle(
        name='BodyText',
        parent=styles['Normal'],
        spaceBefore=6,
        spaceAfter=6,
    )
    # Datos para la tabla
    data = [['ID', 'Nombre','Segundo Nombre','Apellido P.','Apellido M.', 'Email', 'Teléfono']]
    for cliente in clientes:
        data.append([str(cliente.id), cliente.nombre1,cliente.nombre2,cliente.apellido1,cliente.apellido2, cliente.correo_electronico, cliente.celular])

    # Crear la tabla y aplicar los estilos
    table = Table(data)
    table.setStyle(style_table)

    # Agregar la tabla al documento
    styles = getSampleStyleSheet()
    style_heading1 = styles['Heading1']
    elements.append(Paragraph('Informe de Clientes', style_heading1))
    elements.append(table)

    # Generar el documento PDF
    document.build(elements)

    return response