from django.urls import path
from . import views

urlpatterns = [
    path('', views.knowledges_page, name='knowledges_page'),
    path('unit/', views.create_unit, name='create unit'),
    path('unit_<unit_id>/', views.edit_unit, name='edit unit'),
    path('edit_unit/', views.edit_unit, name='edit unit'),
]