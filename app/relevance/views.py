from django.shortcuts import render
from .table import tables
def relevance_page(request):
    return render(request, 'relevance/relevance.html', tables)
