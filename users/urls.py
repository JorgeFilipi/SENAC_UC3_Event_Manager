from django.urls import path, include

import users
from events import views
from users.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register_usuario, name='register'),
    #path('', views.editar_usuario, name='editar_usuario'),
]
