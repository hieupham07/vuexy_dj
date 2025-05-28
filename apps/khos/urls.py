
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.kho_list), name='kho_list'),
    path('create/', login_required(views.kho_create), name='kho_create'),
    path('update/<int:pk>/', login_required(views.kho_update), name='kho_update'),
    path('delete/<int:pk>/', login_required(views.kho_delete), name='kho_delete'),
]