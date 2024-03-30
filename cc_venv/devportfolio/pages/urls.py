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
    path('my-colabs/<int:developer_id>/', views.developer_detail, name='devcolabs'),
    path('my-list/', views.devcolaborators,name='developer_list'),
    path('my-add/', views.developer_add, name='add_dev'),
    path('my-deleted_dev/<int:developer_id>/', views.developer_delete, name='devdelet'),
    path('my-edit_dev/<int:developer_id>/', views.developer_edit, name='devdedit'),


   
]
