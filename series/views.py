from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms

from .models import SeriesThread, SeriesReply, SeriesFileUploaded, Series
from login.models import Person
from groups.models import Group
from courses.models import Course
from forum.models import Forum

import os


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
		"courses_list" : zip ( courses_list, forums ),
		"group_id" : groups,
		"series" : user_data.series
	}


@login_required
def forum_group( request, series_name ):

	forum_series = Series.objects.get( name = series_name )
	threads = SeriesThread.objects.filter( series_id = forum_series.id )

	context = {

		"debug" : "",
		"base_info" : GlobalContext( request ),
		"threads" : threads,
		"series" : forum_series
		
	}

	return render( request, "series/all_threads.html", context )

@login_required
def topic( request, series_name, topic_id ):

	forum = Series.objects.get( name = series_name )

	class CommentForm( forms.Form ):

		desc = forms.CharField( widget = forms.Textarea )
		file = forms.FileField( label = "Attach a file ", widget = forms.ClearableFileInput( attrs = { 'multiple' : True } ), required = False )

	my_comment_form = CommentForm()

	files = SeriesFileUploaded.objects.all().filter( thread = SeriesThread.objects.get( id = topic_id ) )

	for file in files : 

		file.file = str( file.file).rsplit('/', 1)[ 1 ]

	context = {

		"debug" : "",
		"base_info" : GlobalContext( request ),
		"thread" : SeriesThread.objects.get( id = topic_id ),
		"comment_form" : my_comment_form,
		"comments" : SeriesReply.objects.all().filter( replied_to_id = topic_id ),
		"files" : files,

	}

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = CommentForm( request.POST )

		if form.is_valid():

			comment = SeriesReply( 
				desc = form.cleaned_data[ "desc" ],
				author_id = Person.objects.get( user_id = request.user.id ).id,
				replied_to_id = topic_id,
			)

			comment.save()

			files = request.FILES.getlist('file')

			for f in files :

				file = SeriesFileUploaded(

					thread = SeriesThread.objects.all().get( id = topic_id ),
					reply = comment,
					file = f

				)

				file.save()	

	return render( request, "series/thread.html", context )


@login_required
def add_thread( request, series_name ):

	series = Series.objects.get( name = series_name )

	class AddTopicForm( forms.Form ):

		name = forms.CharField( max_length = 100 )
		desc = forms.CharField( widget = forms.Textarea )
		file = forms.FileField( label = "Attach a file ", widget = forms.ClearableFileInput( attrs = { 'multiple' : True } ), required = False )


	my_topic_form = AddTopicForm()

	context = {

		"debug" : "",
		"base_info" : GlobalContext( request ),
		"add_form" : my_topic_form

	}

	if request.method == 'POST':

		# create a form instance and populate it with data from the request:
		form = AddTopicForm( request.POST )

		if form.is_valid() :
			
			topic = SeriesThread( 
				name = form.cleaned_data[ "name" ],
				desc = form.cleaned_data[ "desc" ],
				author_id = Person.objects.get( user_id = request.user.id ).id,
				series_id = series.id,
			)

			topic.save()

			files = request.FILES.getlist('file')

			for f in files :

				file = SeriesFileUploaded(

					thread = topic,
					reply = None,
					file = f

				)

				file.save()
	
	return render( request, "series/add_thread.html", context )	


@login_required
def file( request, file_slug ):

	# get the file

	file_obj = SeriesFileUploaded.objects.get( slug = file_slug )

	file = file_obj.file

	base = os.path.basename( file.path )
	file_name = os.path.splitext( base )

    # get the file data
	data = open( file.path, "rb" ).read()
    
    # download 
	response = HttpResponse( data , content_type='application/vnd')
	response[ 'Content-Length' ] = os.path.getsize( file.path )
	response['Content-Disposition'] = 'filename = ' + str( base ) 

	return response