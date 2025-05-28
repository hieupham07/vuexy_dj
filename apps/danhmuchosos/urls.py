
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

from .views import DanhMucHoSoListView, DanhMucHoSoCreateView, DanhMucHoSoUpdateView, DanhMucHoSoDeleteView

urlpatterns = [
    path("danhmuchosos/", DanhMucHoSoListView.as_view(template_name="danhmuchoso_list.html"), name="danhmuchoso_list"),
    path("danhmuchosos/create/", DanhMucHoSoCreateView.as_view(template_name="danhmuchoso_form.html"), name="danhmuchoso_create"),
    path("danhmuchosos/update/<int:pk>/", DanhMucHoSoUpdateView.as_view(template_name="danhmuchoso_form.html"), name="danhmuchoso_update"),
    path("danhmuchosos/delete/<int:pk>/", DanhMucHoSoDeleteView.as_view(template_name="danhmuchoso_delete.html"), name="danhmuchoso_delete"),
]