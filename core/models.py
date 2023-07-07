from django.db import models
from django.core.exceptions import ValidationError

class Student(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=50)
    total_grade = models.DecimalField(max_digits=5, decimal_places=2)
    rank = models.IntegerField(default=0)

    def clean(self):
        if self.total_grade > 1500:
            raise ValidationError('Total grade cannot be greater than 1500')