from django.db import models
from users.models import CustomUser
import datetime

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=120, blank=False, null=False)
	text = models.TextField()
	date = models.DateTimeField(default=datetime.datetime.now)
	author = models.ForeignKey(CustomUser)

	def __unicode__(self):
		return self.title