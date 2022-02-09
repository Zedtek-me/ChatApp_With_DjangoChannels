from django.urls import path
from . import api_view

urlpatterns=[
    #   api view urls
            path('', api_view.index, name='api index'),
            path('users/', api_view.get_users, name='user handler'),
            path('messages/', api_view.get_messages, name= 'messages handler'),

]