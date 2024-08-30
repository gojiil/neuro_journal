from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_page, name='notes_page'),
    path('note/', views.edit_note, name='create note'),
    path('note_<note_id>/', views.edit_note, name='edit note'),
]