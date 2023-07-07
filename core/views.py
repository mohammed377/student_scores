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
        
        # Get ranks from DB    
        ranked_grades = Student.objects.filter(
            id__in=[g.id for g in grades]
        ).order_by('rank').values_list('rank', flat=True)
        
        # Zip ranks with grades    
        ranked_grades = zip(ranked_grades, grades)

        context = {
            'ranked_grades': ranked_grades  
        }
        
    else:    
        grades = Student.objects.all().order_by('-total_grade')  
        
        # Get ranks from DB    
        ranked_grades = Student.objects.all().order_by('rank').values_list('rank', flat=True)
        
        # Zip ranks with grades    
        ranked_grades = zip(ranked_grades, grades)
        
        context = {
            'ranked_grades': ranked_grades   
        }
    
    return render(request, 'index.html', context)
