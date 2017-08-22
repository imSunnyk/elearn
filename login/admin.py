from django.contrib import admin
from .models import Person, Tutor

class PersonAdmin( admin.ModelAdmin ) : 

	 exclude = ( "hash_code", )

class TutorAdmin( admin.ModelAdmin ) : 

	 exclude = ( "hash_code", )

# register the admin model

admin.site.register( Person, PersonAdmin )
# admin.site.register( Tutor, TutorAdmin )