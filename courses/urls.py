from django.conf.urls import url, include
from . import views

urlpatterns = [
  
	url( r'^/$', views.my_courses, name = "my_courses" ),
	url( r'course/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/$', views.my_course, name = "my_course" ),
	url( r'course_guide/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/$', views.course_guide, name = "course_guide" ),
	url( r'course_resources/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/$', views.course_resources, name = "course_guide" ),
	url( r'course_resources_activities/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/$', views.course_resources_activities, name = "course_guide" ),
	url( r'week/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/(?P<week_slug>[a-zA-Z0-9-_]{5,50})', views.week, name = "week" ),
	url( r'page/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/(?P<week_slug>[a-zA-Z0-9-_]{5,50})/(?P<page_slug>[a-zA-Z0-9-_]{5,50})', views.page, name = "page" )

]
