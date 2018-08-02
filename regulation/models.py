from django.db import models

# Create your models here.

from django.utils import timezone

class RegulationBody(models.Model):
	_id = models.AutoField(primary_key=True)
	_type = models.CharField(max_length=200)
	_content = models.TextField()

	def __str__(self):
		return self._content

