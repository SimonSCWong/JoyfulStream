
# hotels/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


# class CustomUser(AbstractUser):
#       is_staff = models.BooleanField(default=False)
#       is_active = models.BooleanField(default=True)
      
def __str__(self):
    return self.email

def __str__(self):
    return self.paytutorials

class CustomUser(models.Model):
      email = models.CharField(max_length=100)
      password1 = models.CharField(max_length=50)
      confirmed_password = models.CharField(max_length=50)
      

  