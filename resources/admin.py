from django.contrib import admin
from .models import Resource

class FileAdmin( admin.ModelAdmin ):

	exclude = ( "slug", )


admin.site.register( Resource, FileAdmin )