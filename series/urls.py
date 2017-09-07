from django.conf.urls import url, include
from . import views

urlpatterns = [
  
	url( r'(?P<series_name>[a-zA-Z0-9-_]{3})/(?P<topic_id>[0-9-_]{1,1000000})/$', views.topic, name = "topic" ),
	url( r'add_thread/(?P<series_name>[a-zA-Z0-9-_]{3})/$', views.add_thread, name = "add_thread" ),
	url( r'file/(?P<file_slug>[a-zA-Z0-9-_]{32})/$', views.file, name = "file" ),
	url( r'(?P<series_name>[a-zA-Z0-9-_]{3})/$', views.forum_group, name = "forum" ),


]