from django.conf.urls import url, include
from . import views

urlpatterns = [
  
	url( r'(?P<forum_slug>[a-zA-Z0-9-_]{32})/(?P<topic_id>[a-zA-Z0-9-_]{1,100})/$', views.topic, name = "topic" ),
	url( r'add_thread/(?P<forum_slug>[a-zA-Z0-9-_]{32})/$', views.add_thread, name = "add_thread" ),
	url( r'file/(?P<file_slug>[a-zA-Z0-9-_]{32})/$', views.file, name = "file" ),
	url( r'(?P<forum_slug>[a-zA-Z0-9-_]{32})/$', views.forum_group, name = "forum" ),


]