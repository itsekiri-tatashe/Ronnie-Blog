from django.contrib import admin

from .models import Author
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'instagram',"slug")
	list_display_links = ('first_name', 'last_name')
	list_editable = ("slug",)
	list_filter = ("first_name","last_name")
	search_fields = ('first_name', 'last_name')
	list_per_page = 10

	fieldsets = [
		("Your First and Last Name",{"fields":["first_name","last_name"]}),
		("Picture",{"fields":["snap"]}),
		("Your Nickname?? e.g my-lovely-pap",{"fields":["slug"]}),
		("Socials",{"fields":["email","phone",'instagram']}),
		("Mention One Word each that bests describes you",{"fields":["value_1","value_2"]}),
		("Describe Yourself",{"fields":["description"]}),
	]
admin.site.register(Author,AuthorAdmin)