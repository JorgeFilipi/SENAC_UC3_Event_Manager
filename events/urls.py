from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('event_list/', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event_add/', views.event_add, name='event_add'),
    path('event_delete/<int:event_id>/', views.event_delete, name='event_delete'),
    path('inscrit_list/<int:event_id>/', views.inscrit_list, name='inscrit_list'),
]