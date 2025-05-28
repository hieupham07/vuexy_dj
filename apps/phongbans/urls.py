
from django.urls import path
from . import views
from .views import PhongbansView , PhongbanCreateView, PhongbanUpdateView, PhongbanDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path("phongbans/",PhongbansView.as_view(template_name="phongban_list.html"),name="phongban_list"),
    path("phongbans/create/",PhongbanCreateView.as_view(template_name="phongban_form.html"),name="phongban_create"),
    path('phongbans/update/<int:pk>/', PhongbanUpdateView.as_view(template_name="phongban_form.html"), name='phongban_update'),
    path('phongbans/delete/<int:pk>/', PhongbanDeleteView.as_view(template_name="phongban_delete.html"), name='phongban_delete'),

    # path('phongbans/', views.phongban_list, name='phongban_list'),
    # path('phongbans/create/', views.phongban_create, name='phongban_create'),
    # path('phongbans/delete/<int:pk>/', views.phongban_delete, name='phongban_delete'),
    # path(
    #     "app/user/list/",
    #     UsersView.as_view(template_name="app_user_list.html"),
    #     name="app-user-list",
    # ),
]
