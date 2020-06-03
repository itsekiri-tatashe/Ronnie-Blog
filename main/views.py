from django.shortcuts import render

from blog.models import Article
from author.models import Author
# Create your views here.
def home(request):
	article_content = Article.objects.all().order_by("-blog_time").filter(is_published=True)[:3]
	writers = Author.objects.all()
	frontend = {
		"article_content": article_content,
		"writers":writers
	}

	return render(request,"main/home.html",frontend)

def navbar(request):
	return render(request,"base.html",frontend)
