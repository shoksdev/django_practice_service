from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('registration/done/', views.RegisterDoneView.as_view(), name='register_done'),
]
