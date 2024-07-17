from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('academic-record/', views.academic_record, name='academic_record'),
    path('projects/', views.projects, name='projects'),
]
