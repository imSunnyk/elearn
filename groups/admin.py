from django.contrib import admin
from .models import Group
from .forms import GroupFormAdmin

# define the group panel for the admin

class GroupAdmin( admin.ModelAdmin ) :
	form = GroupFormAdmin

	exclude = ( "slug", "name", "group_form_identifier" )

	fieldsets = (
		(None, {
			'fields': ('location', 'course', 'tutors', 'users', 'series', 'group_form_identifier'),
		}),
	)

	search_fields = [ "course__name", "course__code", "location", "series__name" ]

# register the models
admin.site.register( Group, GroupAdmin )