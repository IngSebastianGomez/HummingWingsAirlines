""" API url configuration """
from django.urls import path

from .views.auth import AuthApi, NewPasswordApi, RefreshTokenApi
from .views.root import RootApi
from .views.user import ConfirmRegisterApi, SpecificClientApi, UserApi

urlpatterns = [
    path('auth/', AuthApi.as_view(), name='authentication'),
    path('change_password/<int:user_pk>', NewPasswordApi.as_view(), name='change_password'),
    path('refresh_token/', RefreshTokenApi.as_view(), name='refresh_token'),
    path('root/', RootApi.as_view(), name='root'),
    path('user/', UserApi.as_view(), name='user'),
    path('user/<int:client_pk>', SpecificClientApi.as_view(), name='specific_client'),
    path('user/<int:pk>/confirm_email/<int:token>', ConfirmRegisterApi.as_view(), name='specific_user'),
]