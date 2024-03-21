# pages/urls.py


from django.urls import path
from . import views


# app_name = 'pages'
urlpatterns = [
    # Standalone Web Pages
    path('', views.home, name='home'),
    path('about-me/', views.about, name='about'),
    path('my-services/', views.services, name='services'),
    path('my-contact/', views.contact, name='contact'),
     path('my-colabs/', views.devcolaborators, name='devcolabs'),
   
]
