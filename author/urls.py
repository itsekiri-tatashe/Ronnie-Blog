from django.urls import path

from . import views

app_name = "author"

urlpatterns = [
	path("",views.connect,name="connect"),
	path("<slug:slug>",views.author,name="author"),
]
