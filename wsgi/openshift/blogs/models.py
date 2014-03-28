from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateTimeField('date published')
	content = models.TextField()
	hidden = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.title
	
class Comment(models.Model):
	email_address = models.EmailField()
	parent = models.ForeignKey('Post')
	content = models.TextField()
	date = models.DateTimeField('date submitted',auto_now=True)
	hidden = models.BooleanField(default=True)

	def __unicode__(self):
		return self.content[:49]