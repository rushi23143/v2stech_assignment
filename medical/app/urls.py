from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    ### Store
    path('manage_store/', views.manage_store, name='manage_store'),
    path('add_store/', views.add_store, name='add_store'),
    path('edit_store/<int:id>/', views.edit_store, name='editstore'),
    path('delete_store/<int:id>/',views.delete_store, name='deletestore'),
    ### Medicine
    path('manage_medicine/', views.manage_medicine, name='manage_medicine'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('edit_medicine/<int:id>/', views.edit_medicine, name='editmedicine'),
    path('delete_medicine/<int:id>/',views.delete_medicine, name='deletemedicine'),
]