from django.shortcuts import render

def relevance_page(request):
    return render(request, 'relevance/relevance.html')
