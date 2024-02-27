from django.urls import path
from  . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('logout/', views.logout, name='logout')
]
