from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    all_promotions = Promotion.objects.all()
    html = "<h2>Lista de Promociones</h2><br>"
    for promotion in all_promotions:
        url = str(promotion.id)
        html += "<a href=\"" + url + "\">" + promotion.name + "</a><br>"

    return HttpResponse(html)

def promotionDetails(request, promotion_id):
    promotion = Promotion.objects.get(id= promotion_id)
    html = "<h3>Promoción: </h3>" + promotion_id + "<br>"
    html += "Nombre: " + promotion.name + "<br>"
    html += "Valor: " + str(promotion.value) + "<br>"
    html += "Descripción: " + promotion.description + "<br>"
    html += "Imagen: " + promotion.image + "<br>"
    html += "Categoría: " + promotion.category.name + "<br>"
    return HttpResponse(html)