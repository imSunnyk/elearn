from django.contrib import admin
from .models import Group
from .forms import GroupFormAdmin

# define the group panel for the admin

class GroupAdmin( admin.ModelAdmin ) :
	form = GroupFormAdmin

	exclude = ( 
		"group_slug", 
		"group_name", 
		"group_form_identifier" )

	fieldsets = (
		(None, {
			'fields': (
				'group_location', 
				'group_course', 
				'group_tutors', 
				'group_users', 
				'group_series', 
				'group_form_identifier'),
		}),
	)

	search_fields = [ 
		"group_course__name", 
		"group_course__code", 
		"group_location", 
		"group_series__name" 
	]

# register the models
admin.site.register( Group, GroupAdmin )