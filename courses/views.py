import os

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers

from forum.models import Forum
from login.models import Person
from groups.models import Group
from resources.models import Resource 
from courses.models import Course, Week, Page
from django.contrib.auth.models import User

# define the global context
def GlobalContext( request ):

	user_data = Person.objects.all().get( user_id = request.user.id ) # get the user_data
	student_id = Person.return_student_id( request.user.id ) # get the student id from the user_id
	courses_ids = Person.return_student_courses( student_id ) # get the ids of the courses the student attends
	courses_list = Course.return_courses( courses_ids = courses_ids ) # get the courses
	groups = Group.return_student_group( student_id ) # get the groups the student is part of	
	groups_id = []

	for group in groups :

		groups_id.append( group[ "id" ] )

	forums = Forum.objects.all().filter( group_id__in = groups_id ) 
	

	return {

		"user_data" : user_data,
		"student_id" : student_id,
		"courses_ids" : courses_ids ,
		"courses_list" : zip( courses_list, forums ),
		"group_id" : groups_id,
		"series" : user_data.series
	}

@login_required
def my_courses( request ) :

	context = {

		"debug" : "",
		"base_info" : GlobalContext( request ),

	}

	return render( request, "courses/my_courses.html", context )

@login_required
def my_course( request, course_slug ) :

	my_course = Course.objects.all().get( slug = course_slug )
	weeks = Week.objects.all().filter( course = my_course.id )
	pages = dict()

	# get the id of the group you are in this course
	student_id = Person.return_student_id( request.user.id )
	groups = Group.return_student_group( student_id )
	gr_id = 0
	for group in groups : 

		if group[ "course_id" ] == my_course.id :

			gr_id = group[ "id" ]


	for week in weeks : 

		pages[ week.id ] = Page.objects.all().filter( week = week )

	context = {

		"debug" : "",
		"base_info" : GlobalContext( request ),
		"course" : my_course ,
		"weeks" : weeks,
		"pages" : pages,
		"forum" : Forum.objects.all().get( group_id = gr_id )

	}

	return render( request, "courses/course_plan.html", context )

@login_required
def week( request, course_slug, week_slug ) :
	
	course = Course.objects.all().get( slug = course_slug )
	week = Week.objects.all().get( slug = week_slug, course_id = course ) 
	pages = Page.objects.all().filter( week = week )

	context = {

		"debug" : "",
		"course" : course,
		"week" : week,
		"pages" : pages,
		"base_info" : GlobalContext( request ),

	}

	return render( request, "courses/week.html", context )

@login_required
def page( request, course_slug, week_slug, page_slug ) :

	course = Course.objects.all().get( slug = course_slug )
	week = Week.objects.all().get( slug = week_slug, course_id = course )
	page = Page.objects.all().get( slug = page_slug, week_id = week )

	context = {

		"debug" : "",
		"course" : course,
		"week" : week,
		"page" : page,
		"base_info" : GlobalContext( request ),

	}

	return render( request, "courses/page.html", context )

@login_required
def course_guide( request, course_slug ):
	# get the file

	guide = Course.objects.get( slug = course_slug )

	file = guide.guide

	base = os.path.basename( file.path )
	file_name = os.path.splitext( base )

    # get the file data
	data = open( file.path, "r" )
    
    # download 
	response = HttpResponse( data.read() , content_type='application/pdf')
	response[ 'Content-Length' ] = os.path.getsize( file.path )
	response['Content-Disposition'] = 'inline;filename=some_file.pdf' 

	return response

@login_required
def course_resources( request, course_slug ):

	course = Course.objects.all().get( slug = course_slug )
	resources = Resource.objects.all().filter( course_id = course.id, doc_type = "CO" )

	context = {

		"resources" : resources,
		"course" : course,
		"type" : "Activities resources",
		"link" : "course_resources_activities",
		"base_info" : GlobalContext( request )

	}

	return render( request, "courses/resources.html", context )

@login_required
def course_resources_activities( request, course_slug ):

	course = Course.objects.all().get( slug = course_slug )
	resources = Resource.objects.all().filter( course_id = course.id, doc_type = "AC" )

	context = {

		"resources" : resources,
		"course" : course,
		"type" : "Activities resources",
		"link" : "course_resources_activities",
		"base_info" : GlobalContext( request )

	}

	return render( request, "courses/resources.html", context )


# Ajax views

@login_required
def get_students_by_course( request, course_id ):
	
	student_ids = Person.objects.filter( active_courses = course_id ).values( "user_id" )

	users = list()

	for student_id in student_ids : 

		user = User.objects.get( id = student_id[ "user_id" ]  )

		users.append( user )

	students = serializers.serialize( 
	 	"json", 
	 	users,
	 	fields = ( "username" )
	)

	return HttpResponse( students );