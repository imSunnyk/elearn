import os

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
	group_id = Group.return_student_group( student_id ) # get the groups the student is part of
	forum_slug = Forum.objects.get( group_id = group_id[ 0 ][ "id" ] )	

	return {

		"user_data" : user_data,
		"student_id" : student_id,
		"courses_list" : courses_list,
		"group_id" : group_id,
		"forum_slug" : forum_slug

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

	my_course = Course.objects.all().get( slug = course_slug )
	weeks = Week.objects.all().filter( course = my_course.id )
	pages = dict()

	for week in weeks : 

		pages[ week.id ] = Page.objects.all().filter( week = week )

	context = {

		"debug" : "",
		"base_info" : GlobalContext( request ),
		"course" : my_course ,
		"weeks" : weeks,
		"pages" : pages,

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
