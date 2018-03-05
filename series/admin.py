from django.contrib import admin
from .models import Series

class SeriesAdmin( admin.ModelAdmin ):

	exclude = ( "series_slug", )

	
admin.site.register( Series, SeriesAdmin )