import email

from django.db import models
from django.utils.timezone import now
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    birth_date = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'User'
        ordering = ['first_name']
        

    @property
    def name(self):
        return '{}  {}'.format(self.first_name , self.last_name)

    @property
    def age(self):
        today = now().date()
        dob = self.birth_date
        return today.year - dob.year - (today.timetuple()[1:3] < dob.timetuple()[1:3])
        


