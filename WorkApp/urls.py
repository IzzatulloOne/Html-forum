from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_school, name='add_school'),
    path('add_parent_guardian/', views.add_parent_guardian, name='add_parent_guardian'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_payment/', views.add_payment, name='add_payment'),
]
