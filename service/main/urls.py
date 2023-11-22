from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('application/create/', views.ApplicationCreateView.as_view(), name="application_create"),
    path('application/delete/<int:pk>/', views.ApplicationDeleteView.as_view(), name="application_delete"),

]
