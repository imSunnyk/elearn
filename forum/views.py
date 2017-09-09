import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Forum, Thread, Reply, FileUploaded
from courses.models import Course
from groups.models import Group
from login.models import Person
from .forms import CommentForm, AddTopicForm


@login_required
def forum_group( request, forum_slug ):

	my_forum = Forum.objects.get( forum_slug = forum_slug )
	my_threads = Thread.objects.filter( thread_forum_id = my_forum.id )

	context = {

		"threads" : my_threads,
		"forum" : my_forum,
		"debug" : "",
		
	}

	return render( request, "forum/all_threads.html", context )


@login_required
def topic( request, forum_slug, topic_id ):

	my_forum = Forum.objects.get( forum_slug = forum_slug )
	my_files = FileUploaded.objects.all().filter( 
		file_thread = Thread.objects.get( id = topic_id ) 
	)

	for my_file in my_files : 

		my_file.file = str( my_file.file_file_path).rsplit('/', 1)[ 1 ]

	my_comment_form = CommentForm()

	context = {

		"debug" : "",
		"comments" : Reply.objects.all().filter( reply_replied_to_id = topic_id ),
		"thread" : Thread.objects.get( id = topic_id ),
		"comment_form" : my_comment_form,
		"forum" : my_forum,
		"files" : my_files,

	}

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		my_post_form = CommentForm( request.POST )

		if my_post_form.is_valid():

			my_post_comment = Reply( 
				reply_desc = my_post_form.cleaned_data[ "desc" ],
				reply_author_id = Person.objects.get( user_id = request.user.id ).id,
				reply_replied_to_id = topic_id,
			)

			my_post_comment.save()

			my_post_files = request.FILES.getlist('file')
			for my_post_f in my_post_files :

				my_post_file = FileUploaded(
					file_thread = Thread.objects.all().get( id = topic_id ),
					file_reply_id = my_post_comment.id,
					file_file_path = my_post_f
				)
				my_post_file.save()	

	return render( request, "forum/thread.html", context )


@login_required
def add_thread( request, forum_slug ):

	my_forum = Forum.objects.get( forum_slug = forum_slug )
	my_topic_form = AddTopicForm()

	context = {

		"debug" : "",
		"add_form" : my_topic_form

	}

	if request.method == 'POST':

		# create a form instance and populate it with data from the request:
		my_post_form = AddTopicForm( request.POST )

		if my_post_form.is_valid() :
			
			my_post_topic = Thread( 
				thread_name = my_post_form.cleaned_data[ "name" ],
				thread_desc = my_post_form.cleaned_data[ "desc" ],
				thread_author_id = Person.objects.get( user_id = request.user.id ).id,
				thread_forum_id = my_forum.id,
			)

			my_post_topic.save()

			my_post_files = request.FILES.getlist('file')

			for my_post_f in my_post_files :

				my_post_file = FileUploaded(

					file_thread = my_post_topic,
					file_file_path = my_post_f

				)

				my_post_file.save()
	
	return render( request, "forum/add_thread.html", context )	


@login_required
def file( request, file_slug ):

	# get the file

	my_file_obj = FileUploaded.objects.get( file_slug = file_slug )

	my_file = my_file_obj.file_file_path

	my_base = os.path.basename( my_file.path )
	my_file_name = os.path.splitext( my_base )

    # get the file data
	my_data = open( my_file.path, "rb" ).read()
    
    # download 
	response = HttpResponse( my_data , content_type='application/vnd')
	response[ 'Content-Length' ] = os.path.getsize( my_file.path )
	response['Content-Disposition'] = 'filename = ' + str( my_base ) 

	return response
