from django.urls import path
from . import views


app_name = 'films'
urlpatterns = [
    path('', views.main, name='main'),
    path('user_info/', views.user_info, name='user_info'),
    ## new route below ##
    path('user_form/', views.user_form, name= 'user_form'),
    path('<int:id>/details', views.details, name='details'),
]