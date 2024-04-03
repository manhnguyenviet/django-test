from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(null=True, blank=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if self.content:
			self.title = self.content[:10]
			self.save(update_fields=["title"]) # this will cause the save method to be called infinite in case the content has value
