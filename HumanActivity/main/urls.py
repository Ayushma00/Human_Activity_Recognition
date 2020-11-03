from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name='index1'),
    path("predict1",views.predict1,name='predict1')
]
