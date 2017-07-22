from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from login.models import Person
from groups.models import Group
from courses.models import Course
from django.contrib.auth.models import User

# define the global context
def GlobalContext( request ):

	user_data = Person.objects.all().get( user_id = request.user.id ) # get the user_data
	student_id = Person.return_student_id( request.user.id ) # get the student id from the user_id
	courses_ids = Person.return_student_courses( student_id ) # get the ids of the courses the student attends
	courses_list = Course.return_courses( courses_ids = courses_ids ) # get the courses
	group_id = Group.return_student_group( student_id ) # get the groups the student is part of	

	return {

		"user_data" : user_data,
		"student_id" : student_id,
		"courses_list" : courses_list,
		"group_id" : group_id

	}

@login_required
def my_courses( request ) :

	context = {

		"debug" : "",
		"base_info" : GlobalContext( request )

	}

	return render( request, "courses/my_courses.html", context )

@login_required
def my_course( request, course_slug ) :

	context = {

		"debug" : "",
		"base_info" : GlobalContext( request )

	}

	return render( request, "courses/course_plan.html", context )

def week( request, course_slug, week_slug ) :

	return render( request, "courses/week.html" )


def page( request, week_slug, page_slug ) :

	return render( request, "courses/page.html" )