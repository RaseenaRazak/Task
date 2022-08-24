from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('details/',views.dist_load,name='person_details'),
    path('submit/',views.view_message,name="submit")

]
