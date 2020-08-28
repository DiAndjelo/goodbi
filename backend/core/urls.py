from django.urls import path
from core.views import PassengerListView, PassengerView


urlpatterns = [
    path('', PassengerListView.as_view(), name='passenger_list'),
    path('data.json/', PassengerView.as_view(), name='passengers')
]
