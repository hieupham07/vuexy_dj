
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import DanhMucTaiLieuListView, DanhMucTaiLieuCreateView, DanhMucTaiLieuUpdateView, DanhMucTaiLieuDeleteView

urlpatterns = [
    path('danhmuctailieus/', DanhMucTaiLieuListView.as_view(template_name="danhmuctailieu_list.html"), name='danhmuctailieu_list'),
    path('danhmuctailieus/create/', DanhMucTaiLieuCreateView.as_view(template_name="danhmuctailieu_form.html"), name='danhmuctailieu_create'),
    path('danhmuctailieus/update/<int:pk>/', DanhMucTaiLieuUpdateView.as_view(template_name="danhmuctailieu_form.html"), name='danhmuctailieu_update'),
    path('danhmuctailieus/delete/<int:pk>/', DanhMucTaiLieuDeleteView.as_view(template_name="danhmuctailieu_delete.html"), name='danhmuctailieu_delete'),
]