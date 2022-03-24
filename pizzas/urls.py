from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
			#Homepage link
			path('', views.index, name='index'),
			#Pizzza link.
			path('pizzas/', views.pizzas, name='pizzas'),
			#pizza link
			path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]