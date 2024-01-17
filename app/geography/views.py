from django.shortcuts import render

def geography_page(request):
    return render(request, 'geography/geography.html')
