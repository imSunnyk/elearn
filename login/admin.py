from django.contrib import admin
from .models import Person, Tutor

class PersonAdmin( admin.ModelAdmin ) : 

	pass

class TutorAdmin( admin.ModelAdmin ) : 

	pass

# register the admin model

admin.site.register( Person, PersonAdmin )
admin.site.register( Tutor, TutorAdmin )