from django.contrib import admin
from .models import Series

class SeriesAdmin( admin.ModelAdmin ):

	pass

	
admin.site.register( Series, SeriesAdmin )