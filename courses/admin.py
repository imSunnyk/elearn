from django.contrib import admin

from .models import Course, Week, Book, Subchapter, Page
from .forms import PageForm, CourseForm
from resources.models import Resource


class CourseAdmin( admin.ModelAdmin ) : 

	form = CourseForm
	exclude = ( "course_slug", )
	search_fields = [

		"course_name",
		"course_code"

	]


class WeekAdmin( admin.ModelAdmin ) : 

	exclude = ( "week_slug", )
	search_fields = [

		"week_name",	
		"week_course__course_name",
		"week_course__course_code",

	]


class BookAdmin( admin.ModelAdmin ):

	exclude = ( "book_slug", )
	search_fields = [
	
		"book_name", 
		"book_week__week_name", 
		"book_week__week_course__course_name", 
		"book_week__week_course__course_code" 

	]


class SubchAdmin( admin.ModelAdmin ) :

	exclude = ( "subch_slug", )
	search_fields = [

		"subch_name,"
		"subch_book__book_name", 
		"subch_book__book_week__week_name", 
		"subch_book__book_week__week_course__course_name", 
		"subch_book__book_week__week_course__course_code" 

	]


class PageAdmin( admin.ModelAdmin ) : 

	form = PageForm
	exclude = ( "page_slug", )
	search_fields = [

		"page_name",
		"page_subch__subch_name",
		"page_subch__subch_book__book_name", 
		"page_subch__subch_book__book_week__week_name", 
		"page_subch__subch_book__book_week__week_course__course_name", 
		"page_subch__subch_book__book_week__week_course__course_code",
		"page_book__book_name", 
		"page_book__book_week__week_name", 
		"page_book__book_week__week_course__course_name", 
		"page_book__book_week__week_course__course_code" ,
 
	]


class FileAdmin( admin.ModelAdmin ):

	exclude = ( "file_slug", )
	search_fields = [ "course__course_name" ]


admin.site.register( Course, CourseAdmin )
admin.site.register( Week, WeekAdmin )
admin.site.register( Book, BookAdmin )
admin.site.register( Subchapter, SubchAdmin )
admin.site.register( Page, PageAdmin )
admin.site.register( Resource, FileAdmin )


