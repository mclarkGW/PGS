from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('pgs/new/', views.pgs_new, name='pgs_new'),
    path('pgs/', views.pgs_all, name='pgs_all'),
    path('pgs/<int:pk>/', views.pgs_new, name='pgs_edit'),
    path('pgs/<int:pk>/delete/', views.pgs_delete, name='pgs_delete'),

    #URL for API Call for PowerAutomate
    path('api/profiles/', views.profiles_api, name='profiles_api'),
]