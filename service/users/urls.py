from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('registration/done/', views.RegisterDoneView.as_view(), name='register_done'),
]
