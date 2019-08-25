# wedding_planner/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('gifts/', TemplateView.as_view(template_name='gifts.html'), name='gifts'),
    path('admin/', admin.site.urls),
    path('dashboard/', include(('dashboard.urls', 'dashboard'))),
    path('users/', include('django.contrib.auth.urls')),
]
