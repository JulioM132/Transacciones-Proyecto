from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="tienda"),
	path('cart/', views.cart, name="carro"),
	path('checkout/', views.checkout, name="revision"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),


]
