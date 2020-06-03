from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Article
# Create your views here.
def posts(request):
	article_content = Article.objects.order_by("-blog_time").filter(is_published=True)

	paginator = Paginator(article_content, 4)
	page = request.GET.get('page')
	paged_articles = paginator.get_page(page)

	frontend = {
		"article_content": paged_articles
	}

	return render(request,"blog/posts.html",frontend)

def post(request,slug):
	blog = get_object_or_404(Article, blog_url=slug)
	
	frontend = {
		"blog": blog
	}

	return render(request,"blog/post.html",frontend)