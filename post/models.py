from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
   # This links the post to the user who is currently logged in
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   body = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__ (self):
      #This makes the post look nice in the admin panel
      return self.title
