from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name='Admin'),
    path('login/', views.login, name='Admin Login'),
    path('manage_account/', views.manage_account),
    path('manage_account/<str:action>/', views.manage_account),
    path('new_post/', views.create_post),
    path('manage_post/', views.manage_post),
    path('manage_post/<str:action>', views.manage_post),
    path('dummy/', views.create_dum),
]
