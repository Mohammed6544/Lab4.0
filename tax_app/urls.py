from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:price>/', views.calculate_tax, name='calculate_tax'),
    path('taxrate/', views.show_tax_rate, name='tax_rate'),
]
