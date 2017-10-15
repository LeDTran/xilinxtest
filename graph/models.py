from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    test1 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    test2 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    test3 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    final = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name
