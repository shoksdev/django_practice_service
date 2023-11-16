from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('accounts/', include('users.urls')),
    path('superadmin/', admin.site.urls),
]
