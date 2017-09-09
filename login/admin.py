from django.contrib import admin
from .models import Person, Tutor

class PersonAdmin( admin.ModelAdmin ) : 

	 exclude = ( "person_hash_code", )

class TutorAdmin( admin.ModelAdmin ) : 

	 exclude = ( "person_hash_code", )

# register the admin model

admin.site.register( Person, PersonAdmin )
# admin.site.register( Tutor, TutorAdmin )