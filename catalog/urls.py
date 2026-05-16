from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
]
