from django.urls import re_path
from ContactApp import views

urlpatterns=[
    re_path(r'^contact$',views.contactApi),
    re_path(r'^contact/([0-9]+)$', views.contactApi)
]