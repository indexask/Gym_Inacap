"""CallCenterGamer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from online.views import Index,Inicio,RegisterView,LoginView,ViewRespuestas
from administracion.views import IndexAdmin,BorrarPregunta,GestionUsuarios,EliminarUsuario,ModificarPregunta
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index),
    path('Administracion/', IndexAdmin),
    path('Login/', LoginView.as_view(), name='Login'),
    path('Register/', RegisterView.as_view(), name='Register'),
    path('Inicio/<int:id>', Inicio),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('Respuesta/<int:idUser>/<int:idPregunta>', ViewRespuestas),
    path('BorrarPregunta/<int:idUser>/<int:idPregunta>', BorrarPregunta),
    path('GestionUsuarios/', GestionUsuarios),
    path('EliminarUsuario/<int:idUser>', EliminarUsuario),
    path('ModificarPregunta/<int:idPregunta>', ModificarPregunta),
    path('Logout/', LogoutView.as_view(template_name='logout.html'), name='logout_uppercase'),

    
]
