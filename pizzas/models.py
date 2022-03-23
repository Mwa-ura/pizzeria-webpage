from django.db import models

# Create your models here.
class Pizza(models.Model):
	"""pizza object"""
	name = models.CharField(max_length=100)

	def __str__(self):
		"""Return a string representation of the pizzas name."""
		return self.name

class Topping(models.Model):
	"""Topping object."""
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		"""Return a string representation of topping's name."""
		return self.name 

		