from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.regulation_text, name='regulation_main')
]
