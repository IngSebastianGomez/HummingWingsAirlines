""" API url configuration """
from django.urls import path

from .views.auth import AuthApi, NewPasswordApi, RefreshTokenApi
from .views.root import RootApi
from .views.user import SpecificUserApi, UserApi
from .views.user import ConfirmUserRegisterApi, ConfirmAdminRegisterApi

urlpatterns = [
    path('auth/', AuthApi.as_view(), name='authentication'), #Bien 
    path('change_password/<int:user_pk>', NewPasswordApi.as_view(), name='change_password'), #Sin / mal
    path('refresh_token/', RefreshTokenApi.as_view(), name='refresh_token'), #Sin
    path('root/', RootApi.as_view(), name='root'), #Bien
    path('user/', UserApi.as_view(), name='user'), #Bien
    path('user/<int:user_pk>', SpecificUserApi.as_view(), name='specific_user'), #Bien
    path('user/<int:pk>/confirm_email/<int:token>', ConfirmUserRegisterApi.as_view(), name='specific_user'), #Mal
    path('admin/<int:pk>/confirm_email/<int:token>', ConfirmAdminRegisterApi.as_view(), name='specific_admin')
]