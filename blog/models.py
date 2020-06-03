from datetime import datetime

from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from author.models import Author

# Create your models here.
class Article(models.Model):
	blog_author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
	blog_title = models.CharField(max_length=200)
	blog_content = RichTextUploadingField()
	blog_time = models.DateTimeField(default=datetime.now)
	is_published = models.BooleanField(default=True) 	
	blog_url = models.SlugField(max_length=200)
	short_description = models.CharField(max_length=200)
	blog_photo = models.ImageField(upload_to='assets/%Y/%m/%d/',default='/media/assets/default.jpg', null = True)
    #blog_photo_1 = models.ImageField(upload_to='assets/%Y/%m/%d/',blank =True)

	def __str__(self):
		return self.blog_title
