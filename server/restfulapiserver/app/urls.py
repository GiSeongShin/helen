from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^api/app$', views.init_main_page)
]