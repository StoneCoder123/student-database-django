from django.urls import path
from . import views

urlpatterns = [


    path('', views.home, name='home'),
    path('profile/<str:pk>', views.user_profile, name='profile'),

    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

]
