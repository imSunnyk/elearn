from django.contrib import admin
from .models import Group

# define the group panel for the admin
class GroupAdmin( admin.ModelAdmin ) :

	exclude = ( "slug", "name" )

# register the models
admin.site.register( Group, GroupAdmin )