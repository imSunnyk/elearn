import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django import forms

from .models import SeriesThread, SeriesReply, SeriesFileUploaded, Series
from courses.models import Course
from login.models import Person
from groups.models import Group
from forum.models import Forum

from .forms import CommentForm


@login_required
def forum_group( request, series_name ):

	my_threads = SeriesThread.objects.filter( 
		series_thread_series_id = forum_series.id 
	)
	my_forum_series = Series.objects.get( series_name = series_name )

	context = {

		"debug" : "",
		"threads" : my_threads,
		"series" : my_forum_series
		
	}

	return render( request, "series/all_threads.html", context )


@login_required
def topic( request, series_name, topic_id ):

	my_forum = Series.objects.get( series_name = series_name )

	my_comment_form = CommentForm()

	my_files = SeriesFileUploaded.objects.all().filter( 
		series_file_thread = SeriesThread.objects.get( id = topic_id ) 
	)

	for my_file in my_files : 

		my_file.file = str( my_file.file).rsplit('/', 1)[ 1 ]

	context = {

		"debug" : "",
		"thread" : SeriesThread.objects.get( id = topic_id ),
		"comment_form" : my_comment_form,
		"comments" : SeriesReply.objects.all().filter( 
			series_reply_replied_to_id = topic_id 
		),
		"files" : my_files,

	}

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		my_form = CommentForm( request.POST )

		if my_form.is_valid():

			my_comment = SeriesReply( 
				series_reply_desc = form.cleaned_data[ "desc" ],
				series_reply_author_id = Person.objects.get( 
					user_id = request.user.id 
				).id,
				series_reply_replied_to_id = topic_id,
			)

			my_comment.save()

			my_files = request.FILES.getlist('file')

			for my_f in my_files :

				my_file = SeriesFileUploaded(
					series_file_thread = SeriesThread.objects.all().get( 
						id = topic_id 
					),
					series_file_reply = my_comment,
					series_file_file = f
				)

				my_file.save()	

	return render( request, "series/thread.html", context )


@login_required
def add_thread( request, series_name ):

	my_series = Series.objects.get( name = series_name )
	my_topic_form = AddTopicForm()

	context = {
		"debug" : "",
		"add_form" : my_topic_form
	}

	if request.method == 'POST':

		# create a form instance and populate it with data from the request:
		my_form = AddTopicForm( request.POST )

		if my_form.is_valid() :
			
			my_topic = SeriesThread( 
				series_thread_name = form.cleaned_data[ "name" ],
				series_thread_desc = form.cleaned_data[ "desc" ],
				series_thread_author_id = Person.objects.get( 
					user_id = request.user.id 
				).id,
				series_thread_series_id = series.id,
			)

			my_topic.save()

			my_files = request.FILES.getlist('file')

			for my_f in my_files :

				my_file = SeriesFileUploaded(

					series_file_thread = my_topic,
					series_file_reply = None,
					series_file_file = my_f

				)

				my_file.save()
	
	return render( request, "series/add_thread.html", context )	


@login_required
def file( request, file_slug ):

	# get the file

	my_file_obj = SeriesFileUploaded.objects.get( 
		series_file_slug = file_slug 
	)

	my_file = my_file_obj.series_file_file

	my_base = os.path.basename( my_file.path )
	my_file_name = os.path.splitext( my_base )

    # get the file data
	my_data = open( my_file.path, "rb" ).read()
    
    # download 
	response = HttpResponse( my_data , content_type='application/vnd')
	response[ 'Content-Length' ] = os.path.getsize( my_file.path )
	response['Content-Disposition'] = 'filename = ' + str( my_base ) 

	return response
