from django.urls import path
from .views import Regitraion,login,logoutuser


urlpatterns = [
    path('',Regitraion,name = 'regitraion'),
    path('login/',login,name = 'login'),
    path('logout/',logoutuser,name = 'logout'),
]
