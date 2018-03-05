import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q

from courses.models import Course, Week, Book, Subchapter, Page
from resources.models import Resource 
from login.models import Person, Tutor
from groups.models import Group
from forum.models import Forum


@login_required
def my_courses( request ) :

	context = {

		"debug" : "",

	}

	return render( request, "courses/my_courses.html", context )


@login_required
def my_course( request, course_slug ) :

	student_id = Person.return_student_id( request.user.id )
	try : 
		possible_tutor = Tutor.objects.all().get( person_id = student_id )
	except :
		possible_tutor = 0

	my_course = Course.objects.all().get( course_slug = course_slug )
	my_weeks = Week.objects.all().filter( week_course = my_course.id )


	my_course_group = Group.objects.all().filter( 
		Q( group_users__in = [ student_id ] ) | Q( group_tutors__in = [ possible_tutor ] ),
		group_course_id = my_course.id, 
	)

	my_forum = Forum.objects.all().get( forum_group = my_course_group )
	my_books = Book.objects.all().filter( book_week_id__in = my_weeks )

	context = {

		"debug" : "",
		"course" : my_course ,
		"weeks" : my_weeks,
		"books" : my_books,
		"forum" : my_forum,

	}

	return render( request, "courses/course_plan.html", context )


@login_required
def week( request, course_slug, week_slug ) :
	
	my_course = Course.objects.all().get( course_slug = course_slug )
	my_week = Week.objects.all().get( week_slug = week_slug, week_course_id = my_course ) 
	my_books = Book.objects.all().filter( book_week = my_week )

	context = {

		"debug" : "",
		"course" : my_course,
		"books" : my_books,
		"week" : my_week,

	}

	return render( request, "courses/week.html", context  )


@login_required
def book( request, course_slug, week_slug, book_slug ) :

	my_course = Course.objects.all().get( course_slug = course_slug )
	my_week = Week.objects.all().get( week_slug = week_slug, week_course = my_course )
	my_book = Book.objects.all().get( book_slug = book_slug, book_week = my_week )
	my_subchapters = Subchapter.objects.all().filter( subch_book = my_book )
	my_pages = Page.objects.all().filter( page_book = my_book )

	context = {

		"debug" : "",
		"subchapters" : my_subchapters ,
		"course" : my_course,
		"pages" : my_pages ,
		"week" : my_week,
		"book" : my_book,

	}

	return render( request, "courses/book.html", context )


@login_required
def course_guide( request, course_slug ):
	# get the file

	my_guide = Course.objects.get( course_slug = course_slug )

	my_file = my_guide.course_guide

	my_base = os.path.basename( my_file.path )
	my_file_name = os.path.splitext( my_base )

    # get the file data
	my_data = open( my_file.path, "r" )
    
    # download 
	response = HttpResponse( my_data.read() , content_type='application/pdf')
	response[ 'Content-Length' ] = os.path.getsize( my_file.path )
	response['Content-Disposition'] = 'inline;filename=some_file.pdf' 

	return response


@login_required
def course_resources( request, course_slug ):

	my_course = Course.objects.all().get( course_slug = course_slug )
	my_resources = Resource.objects.all().filter( 
		resource_course_id = my_course.id, 
		resource_doc_type = "CO"
	)

	context = {

		"link" : "course_resources_activities",
		"type" : "Activities resources",
		"resources" : my_resources,
		"course" : my_course,

	}

	return render( request, "courses/resources.html", context )


@login_required
def course_resources_activities( request, course_slug ):

	my_course = Course.objects.all().get( course_slug = course_slug )
	my_resources = Resource.objects.all().filter( 
		resource_course_id = my_course.id, 
		resource_doc_type = "AC"
	)

	context = {

		"link" : "course_resources_activities",
		"type" : "Activities resources",
		"resources" : my_resources,
		"course" : my_course,

	}

	return render( request, "courses/resources.html", context )


# Ajax views

@login_required
def get_students_by_course( request, course_id ):
	
	my_student_ids = Person.objects.filter( active_courses = course_id ).values( "user_id" )
	my_users = list()

	for my_student_id in my_student_ids : 

		my_user = User.objects.get( id = my_student_id[ "user_id" ]  )
		my_users.append( my_user )

	my_students = serializers.serialize( 
	 	"json", 
	 	my_users,
	 	fields = ( "username" )
	)

	return HttpResponse( my_students );