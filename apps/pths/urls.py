from django.urls import path

from .views import PthsView


urlpatterns = [
    path(
        "trang-chu/",
        PthsView.as_view(template_name="trang_chu.html"),
        name="trang_chu",
    )
]
