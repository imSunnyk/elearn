from django.conf.urls import url, include
from . import views

urlpatterns = [
  

	url( r'resource/(?P<resource_slug>[a-zA-Z0-9-_]{32})', views.resource, name = "resource" ),
]
