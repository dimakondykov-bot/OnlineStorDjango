from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='home'),
    path('product/<int:product_id>/', views.get_product, name='get_product'),
    path('contacts/', views.contacts, name='contacts')
]
