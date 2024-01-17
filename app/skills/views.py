from django.shortcuts import render

def skills_page(request):
    return render(request, 'skills/skills.html')
