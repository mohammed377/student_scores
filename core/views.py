from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from .models import Student
def home(request):  
    if request.GET.get('search'):
        search_term = request.GET.get('search')
        grades = Student.objects.filter(
           Q(name__icontains=search_term) | Q(student_id__contains=search_term)
       ).order_by('-total_grade')
    else:    
        grades = Student.objects.all().order_by('-total_grade')
        
    count = Student.objects.count()   
    return render(request, 'index.html', context={'grades':grades,'count': count})


