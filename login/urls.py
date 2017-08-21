from django.conf.urls import url
from . import views

urlpatterns = [

  	url( r'^login/change_pass/(?P<hash_code>[a-zA-Z0-9-_]{32})$', views.change_pass, name = 'change_pass' ),
	url( r'^login/send_email$', views.send_email, name = 'send_email' ),
	url( r'^login/logout$', views.logout_user, name = 'logout' ),
	url( r'^$', views.login_page, name = 'login' )

]