from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('getEvents',views.getEvents,name='get events as json'),
    path('add',views.add,name='add event')
]