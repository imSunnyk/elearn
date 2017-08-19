from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms

from .models import Forum, Thread, Reply
from login.models import Person
from groups.models import Group
from courses.models import Course


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
	}


@login_required
def forum_group( request, forum_slug ):

	forum = Forum.objects.get( slug = forum_slug )
	threads = Thread.objects.filter( forum_id = forum.id )

	context = {

		"debug" : "",
		"forum" : forum,
		"base_info" : GlobalContext( request ),
		"threads" : threads
		
	}

	return render( request, "forum/all_threads.html", context )

@login_required
def topic( request, forum_slug, topic_id ):

	forum = Forum.objects.get( slug = forum_slug )

	class CommentForm( forms.Form ):

		desc = forms.CharField( widget = forms.Textarea )

	my_comment_form = CommentForm()

	context = {

		"base_info" : GlobalContext( request ),
		"thread" : Thread.objects.get( id = topic_id ),
		"comment_form" : my_comment_form,
		"comments" : Reply.objects.all().filter( replied_to_id = topic_id ),
		"forum" : forum

	}

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = CommentForm( request.POST )

		if form.is_valid():

			comment = Reply( 
				desc = form.cleaned_data[ "desc" ],
				author_id = Person.objects.get( user_id = request.user.id ).id,
				replied_to_id = topic_id
			)

			comment.save()

	return render( request, "forum/thread.html", context )


@login_required
def add_thread( request, forum_slug ):

	forum = Forum.objects.get( slug = forum_slug )

	class AddTopicForm( forms.Form ):

		name = forms.CharField( max_length = 100 )
		desc = forms.CharField( widget = forms.Textarea )


	my_topic_form = AddTopicForm()

	context = {

		"debug" : "",
		"base_info" : GlobalContext( request ),
		"add_form" : my_topic_form

	}

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = AddTopicForm( request.POST )

		if form.is_valid():

			topic = Thread( 
				name = form.cleaned_data[ "name" ],
				desc = form.cleaned_data[ "desc" ],
				author_id = Person.objects.get( user_id = request.user.id ).id,
				forum_id = forum.id
			)

			topic.save()


	return render( request, "forum/add_thread.html", context )	