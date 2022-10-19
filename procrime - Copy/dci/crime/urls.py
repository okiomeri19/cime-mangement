from django.urls import path
from.import views
app_name = "crime"
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('registercrime/',views.registercrime,name='registercrime'),
    
    
]
