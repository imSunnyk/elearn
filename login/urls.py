from django.conf.urls import url
from . import views

urlpatterns = [

  url( r'^login/change_pass$', views.change_pass, name = 'change_pass' ),
	url( r'^login/logout$', views.logout_user, name = 'logout' ),
	url( r'^$', views.login_page, name = 'login' )

]