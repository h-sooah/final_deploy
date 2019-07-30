from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.userlogin, name="userlogin"),
    path('logout/', views.logout, name="logout"),
]