    
from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('criarbolos',ModelBolosCreateView.as_view(),name='criarbolos'),
    path('listadedoces',ModelBolosListView.as_view(),name='listadedoces'),
    path('updatedebolos/<pk>',ModelBolosUpdateView.as_view(),name='updatedebolos'),
]