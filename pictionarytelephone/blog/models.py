from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField("uploaded image", upload_to="images/%Y/%m/%d", blank=True, null=True)
  caption = models.TextField()
  created = models.DateTimeField()
  tags = TaggableManager()
  
  
  def __unicode__(self):
    return self.title