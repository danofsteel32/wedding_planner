from django.urls import path

from . import views

urlpatterns = [
    # /dashboard/
    path('', views.index, name='index'),
    # /dashboard/1/
    path('<int:party_id>/', views.details, name='details'),
    # /dashboard/1/edit/
    path('<int:party_id>/edit/', views.edit, name='edit'),
    # /dashboard/add/
    path('add/', views.add, name='add'),
    # /dashboard/addnew/
    path('addnew/', views.addnew, name='addnew'),
]
