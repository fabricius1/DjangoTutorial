# inside project/urls.py
from django.contrib import admin
from django.urls import path, include
from films import views    # added 


urlpatterns = [
    path('', views.home, name='home'),    # added
    path('admin/', admin.site.urls),
    path('films/', include('films.urls')), 
    # new route: 
    path('gapminder/<int:year>', views.gapminder, name='gapminder'),
]