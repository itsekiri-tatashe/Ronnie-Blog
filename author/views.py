from django.shortcuts import get_object_or_404,render

from .models import Author
# Create your views here.
def connect(request):
	writers = Author.objects.all()
	frontend = {
		"writers":writers
	}

	return render(request,"author/connect.html",frontend)

def author(request,slug):
	writers = get_object_or_404(Author, slug=slug)
	frontend = {
		"writers": writers
	}
	return render(request,"author/author.html",frontend)