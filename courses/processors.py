from django.contrib.auth.models import User

from .models import Course, Week, Book, Subchapter, Page
from resources.models import Resource 
from forum.models import Forum
from login.models import Person
from groups.models import Group

def courseinfo( request ) :

	try :

		my_user_data = User.objects.all().get( id = request.user.id ) 
		my_student_data = Person.objects.all().get( user_id = request.user.id ) 
		my_courses_ids = Person.return_student_courses( my_student_data.id ) 
		my_courses_list = Course.return_courses( courses_ids = my_courses_ids )     
		
		my_groups = Group.return_student_group( my_student_data.id )	
		my_forums = Forum.objects.all().filter( group_id__in = my_groups )

		return {

			"user_data" : my_user_data,
			"student_data" : my_student_data,
			"student_id" : my_student_data.id,
			"courses_ids" : my_courses_ids ,
			"courses_list" : zip( my_courses_list, my_forums ),
			"series" : my_student_data.series
		}

	except : 

		return {}