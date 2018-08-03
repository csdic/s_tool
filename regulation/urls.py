from django.conf.urls import url
from . import view

urlpatterns = [
	url(r'^$',view.regulation_text, name='regulation_main')
]
