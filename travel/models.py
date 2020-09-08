from django.db import models

class Dest(models.Model):
	
	name=models.CharField(max_length=50)
	desc=models.TextField()
	img= models.ImageField(upload_to='pics')
	price=models.IntegerField()
	offer= models.BooleanField(default=False)

# Create your models here.
