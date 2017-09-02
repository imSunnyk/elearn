from django.contrib import admin

from .models import Course, Week, Page
from .forms import PageForm, CourseForm
from resources.models import Resource


# define the courses panel for the admin
class CourseAdmin( admin.ModelAdmin ) : 

	form = CourseForm
	exclude = ( "slug", )

# define the courses panel for the admin
class WeekAdmin( admin.ModelAdmin ) : 

	exclude = ( "slug", )
	search_fields = [ "course__name" ]


# define the courses panel for the admin
class PageAdmin( admin.ModelAdmin ) : 

	form = PageForm
	exclude = ( "slug", )
	search_fields = [ "week__name" ]
	
class FileAdmin( admin.ModelAdmin ):

	exclude = ( "slug", )
	search_fields = [ "course__name" ]

# register the models
admin.site.register( Course, CourseAdmin )
admin.site.register( Week, WeekAdmin )
admin.site.register( Page, PageAdmin )
admin.site.register( Resource, FileAdmin )


