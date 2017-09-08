from django.conf.urls import url, include
from . import views

urlpatterns = [
  
	url( r'^/$', views.my_courses, name = "my_courses" ),
	url( r'course/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/$', views.my_course, name = "my_course" ),
	url( r'course_guide/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/$', views.course_guide, name = "course_guide" ),
	url( r'course_resources/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/$', views.course_resources, name = "course_guide" ),
	url( r'course_resources_activities/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/$', views.course_resources_activities, name = "course_guide" ),
	url( r'week/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/(?P<week_slug>[a-zA-Z0-9-_]{5,50})', views.week, name = "week" ),
	url( r'book/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/(?P<week_slug>[a-zA-Z0-9-_]{5,50})/(?P<book_slug>[a-zA-Z0-9-_]{32})', views.book, name = "book" ),
	url( r'get_students_by_course/(?P<course_id>[0-9]{1,3})', views.get_students_by_course, name = "get_students_by_course" )

]
