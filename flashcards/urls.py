from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.flashcard_list, name='list'),
    path('category/<int:category_id>/', views.flashcard_category, name='category'),
    path('card/<int:flashcard_id>/', views.flashcard_view, name='view'),
    path('random/', views.random_flashcard, name='random'),
]