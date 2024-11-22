from django.urls import path, include
from users import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register_usuario, name='register'),
    path('editar-usuario/', views.editar_usuario, name='editar_usuario'),
]
