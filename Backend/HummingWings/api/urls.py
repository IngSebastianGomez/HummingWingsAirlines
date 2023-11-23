""" API url configuration """
from django.urls import path

from Backend.HummingWings.api.views.booking_holder import BookingHolderApi

from .views.auth import AuthApi, NewPasswordApi, RefreshTokenApi
from .views.card import CardApi, SpecificCardApi, UserCardApi
from .views.flight import FlightApi, SpecificFlightApi
from .views.root import RootApi
from .views.search import PublicFlightApi
from .views.user import SpecificUserApi, UserApi, AdminApi
from .views.user import ConfirmUserRegisterApi, ConfirmAdminRegisterApi

urlpatterns = [
    path('change_password/<int:user_pk>', NewPasswordApi.as_view(), name='change_password'),
    path('auth/', AuthApi.as_view(), name='authentication'),
    path('refresh_token/', RefreshTokenApi.as_view(), name='refresh_token'),
    path('root/', RootApi.as_view(), name='root'), 
    path('user/', UserApi.as_view(), name='user'),
    path('user/cards', UserCardApi.as_view()),
    path('admin/', AdminApi.as_view(), name='user'),
    path('user/<int:user_pk>', SpecificUserApi.as_view(), name='specific_user'),
    path('user/<int:pk>/confirm_email/<int:token>', ConfirmUserRegisterApi.as_view(), name='specific_user'),
    path('admin/<int:pk>/confirm_email/<int:token>', ConfirmAdminRegisterApi.as_view(), name='specific_admin'),
    path('search/flight', PublicFlightApi.as_view()),
    path('flight', FlightApi.as_view()),
    path('flight/<int:flight_id>', SpecificFlightApi.as_view()),
    path('card', CardApi.as_view()),
    path('card/<int:card_id>', SpecificCardApi.as_view()),
    path('booking', BookingHolderApi.as_view()),
    path('payment', SpecificCardApi.as_view()),
]