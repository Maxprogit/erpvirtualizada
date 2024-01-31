from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='web'

urlpatterns=[
    path('login/', views.login, name="login"),   
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.inicio, name="inicio"),
    path('registro/', views.registro, name="registro"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)