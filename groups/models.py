from __future__ import unicode_literals

from django.template.defaultfilters import slugify
from django.db import models

from login.models import Person, Tutor
from courses.models import Course
from series.models import Series


class Group( models.Model ):

	group_name = models.CharField( max_length = 100 )
	group_slug = models.SlugField()
	group_location = models.CharField( max_length = 50 )
	group_course = models.ForeignKey( 
		Course,
		related_name = 'group_course',
	)
	group_tutors = models.ManyToManyField(
		Tutor, 
		related_name = 'group_tutors',
	)
	group_users = models.ManyToManyField( 
		Person, 
		related_name = 'group_users', 
	)
	group_series = models.ForeignKey( 
		Series, 
		related_name = 'group_series',
	)

	# override the save function
	def save( self, *args, **kwargs ):

		ok = 0

		if not self.id:

			from forum.models import Forum
			
			# iterate group name
			possible_groups = Group.objects.all().filter( 
				group_location = self.group_location, 
				group_course = self.group_course, 
				group_series = self.group_series 
			)
			iterator = len( possible_groups )

			# forum creation
			course_code = Course.objects.all().get( 
				id = self.group_course.id 
			).course_code
			self.group_name = "Grupa " + str( iterator ) + "  " + str( course_code ) + " " + str( self.group_location ) + " " + str( self.group_series )

			# Newly created object, so set slug
			self.group_slug = slugify( self.group_name )

			forum_name = "Forum-" + str( self.group_name )
			
			try : 

				# try to find the last group,
				# if not, means this is the first group created
				last_group_id = Group.objects.latest( "id" ).id
				
				group_forum = Forum( 
					forum_name = forum_name, 
					forum_group_id = last_group_id + 1, 
					forum_series_id = self.group_series.id 
				)
				
				forum.save()

			except : 

				forum = Forum( 
					forum_name = forum_name, 
					forum_group_id = 1, 
					forum_series_id = self.group_series.id 
				)
				
				forum.save()
		
		super( Group, self ).save( *args, **kwargs )


	def __unicode__( self ) : 

		return " %s " % ( self.group_name)

	@classmethod
	def return_student_group( self, stundent_id ):

		print self.objects.values( 
			"group_name", 
			"id", 
			"group_course_id" 
		).filter( group_users = stundent_id ).values_list( "id" )

		return self.objects.values( 
			"group_name", 
			"id", 
			"group_course_id" 
		).filter( group_users = stundent_id ).values_list( "id" )