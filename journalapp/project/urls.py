from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_page, name='notes_page'),
    path('project/', views.edit_project, name='create project'),
    path('project_<note_id>/', views.edit_project, name='edit project'),
]