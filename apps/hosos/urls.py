
from django.urls import path
from . import views
from .views import HoSosView , HoSoCreateView, HoSoUpdateView, HoSoDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path("hosos/",HoSosView.as_view(template_name="hoso_list.html"),name="hoso_list"),
    path("hosos/create/",HoSoCreateView.as_view(template_name="hoso_form.html"),name="hoso_create"),
    path('hosos/update/<int:pk>/', HoSoUpdateView.as_view(template_name="hoso_form.html"), name='hoso_update'),
    path('hosos/delete/<int:pk>/', HoSoDeleteView.as_view(template_name="hoso_delete.html"), name='hoso_delete'),
]
