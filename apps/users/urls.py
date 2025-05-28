from django.urls import path
from .views import UsersView
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView

# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login/')

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    # path('users/login/', UserDeleteView.as_view(), name='user_login'),
    path(
        "app/user/list/",
        UsersView.as_view(template_name="app_user_list.html"),
        name="app-user-list",
    ),
    path(
        "app/user/view/account/",
        UsersView.as_view(template_name="app_user_view_account.html"),
        name="app-user-view-account",
    ),
    path(
        "app/user/view/security/",
        UsersView.as_view(template_name="app_user_view_security.html"),
        name="app-user-view-security",
    ),
    path(
        "app/user/view/billing/",
        UsersView.as_view(template_name="app_user_view_billing.html"),
        name="app-user-view-billing",
    ),
    path(
        "app/user/view/notifications/",
        UsersView.as_view(template_name="app_user_view_notifications.html"),
        name="app-user-view-notifications",
    ),
    path(
        "app/user/view/connections/",
        UsersView.as_view(template_name="app_user_view_connections.html"),
        name="app-user-view-connections",
    ),
]
