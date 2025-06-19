from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('medical/', views.medical, name='medical'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('industrial/', views.industrial, name='industrial'),
    path('<slug:category>/', views.category_detail, name='category_detail'),
]