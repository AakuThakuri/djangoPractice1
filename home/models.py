from django.db import models

# Create your models here.
class Information(models.Model):
	address = models.CharField(max_length = 500 )
	area = models.CharField(max_length = 500)
	phone = models.CharField(max_length = 200)
	time = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 500)


	def __str__(self):
		return self.address

class contact(models.Model):
	name = models.CharField(max_length = 500)
	email = models.EmailField(max_length = 500, blank = True )
	subject = models.TextField()
	message = models.TextField()

	def __str__(self):
		return self.name
