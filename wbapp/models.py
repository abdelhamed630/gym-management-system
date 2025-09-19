from django.db import models
from django.utils import timezone
from datetime import timedelta

class Category(models.Model):
    name=models.CharField( max_length=100)
    create_at=models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return self.name
    
class record(models.Model):
    name=models.CharField( max_length=50)
    phone=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    tall=models.IntegerField()
    wedight=models.IntegerField()
    adderss=models.CharField( max_length=500)
    create_at=models.DateTimeField( auto_now_add=True)
    last_payment = models.DateField(default=timezone.now, null=True, blank=True)


    @property
    def is_active(self):
        if self.last_payment:
          return timezone.now().date() - self.last_payment <= timedelta(days=30)
        return False
    
    @property
    def days_left(self):
     if self.last_payment:
        days_passed = (timezone.now().date() - self.last_payment).days
        return max(0, 30 - days_passed)  # لو أقل من 0 يرجع 0
     return 0

    def __str__(self):
        return f"{self.name} "
