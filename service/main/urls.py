from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('application/create/', views.ApplicationCreateView.as_view(), name="application_create"),
    path('application/delete/<int:pk>/', views.ApplicationDeleteView.as_view(), name="application_delete"),
    path('applications/', views.ApplicationListView.as_view(), name="applications_list"),
    path('application/change/status/done/<int:pk>/', views.ApplicationUpdateStatusDoneView.as_view(),
         name="application_change_status_done"),
    path('application/change/status/inwork/<int:pk>/', views.ApplicationUpdateStatusInWorkView.as_view(),
         name="application_change_status_inwork"),
    path('categories/', views.CategoryListView.as_view(), name="categories_list"),
    path('category/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('category/delete/<int:pk>/', views.category_delete, name="category_delete"),
]
