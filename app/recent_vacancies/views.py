from django.shortcuts import render

def recent_page(request):
    return render(request, 'recent_vacancies/recent_vacancies.html')
