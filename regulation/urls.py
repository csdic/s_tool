from django.conf.urls import urls
from . import views

urlpatterns = [
	url(r'^$',view.regulation_text, name='regulation_main')
]
