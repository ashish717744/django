 

from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage),
    path('biodata/',views.biodata),
    path('count1/',views.count,name ='count'),

]
