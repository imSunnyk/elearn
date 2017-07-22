from django.conf.urls import url, include
from . import views

urlpatterns = [
  
	url( r'^/$', views.my_courses, name = "my_courses" ),
	url( r'course/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/$', views.my_course, name = "my_course" ),
	url( r'week/(?P<course_slug>[a-zA-Z0-9-_]{5,50})/(?P<week_slug>[a-zA-Z0-9-_]{5,50})', views.week, name = "week" ),
	url( r'page/(?P<week_slug>[a-zA-Z0-9-_]{5,50})/(?P<page_slug>[a-zA-Z0-9-_]{5,50})', views.page, name = "page" )

]
