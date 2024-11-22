from django.urls import path
from events import views


urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.event_list, name='event_list'),
    path('event/', views.event_add, name='event_add'),
    path('detalhedoevento/<int:event_id>/', views.event_detalhe, name='event_detalhe'),
    path('inscrit_add/<int:event_id>/', views.inscrit_add, name='inscrit_add'),
    path('event_delete/<int:event_id>/', views.event_delete, name='event_delete'),
    path('inscricao/delete/<int:id>/', views.delete_inscricao, name='event_delete_inscription'),
]