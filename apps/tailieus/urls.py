
from django.urls import path
from . import views
from .views import TaiLieuListView , TaiLieuCreateView, TaiLieuUpdateView, TaiLieuDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('tailieus/', TaiLieuListView.as_view(template_name="tailieu_list.html"), name='tailieu_list'),
    path('tailieus/create/', TaiLieuCreateView.as_view(template_name="tailieu_form.html"), name='tailieu_create'),
    path('tailieus/update/<int:pk>/', TaiLieuUpdateView.as_view(template_name="tailieu_form.html"), name='tailieu_update'),
    path('tailieus/delete/<int:pk>/', TaiLieuDeleteView.as_view(template_name="tailieu_delete.html"), name='tailieu_delete'),
]