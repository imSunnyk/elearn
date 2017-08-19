from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from courses.models import Course
from login.models import Person, Tutor
from series.models import Series


class Group( models.Model ):

	name = models.CharField( max_length = 50 )
	slug = models.SlugField()
	location = models.CharField( max_length = 50 )
	course = models.ForeignKey( Course, related_name = 'course' )
	tutors = models.ManyToManyField( Tutor, related_name = 'tutors' )
	users = models.ManyToManyField( Person, related_name = 'users' )
	series = models.ForeignKey( Series, related_name = 'series' )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:
			from forum.models import Forum
			code = Course.objects.all().get( id = self.course.id ).code

			self.name = "Grupa " + str( code ) + " " + str( self.location ) + " " + str( self.series )

			# Newly created object, so set slug
			self.slug = slugify( self.name )

			forum_name = "Forum-" + str( self.name )
			
			try : 

				# try to find the last group, if not, means this is the first group created
				last_group_id = Group.objects.latest( "id" ).id
				
				forum = Forum( name = forum_name, group_id = last_group_id + 1 )
				forum.save()

			except : 

				forum = Forum( name = forum_name, group_id = 1 )
				forum.save()
			

		super( Group, self ).save( *args, **kwargs )
		

	def __unicode__( self ) : 

		return " %s " % ( self.name)

	@classmethod
	def return_student_group( self, stundent_id ):

		return self.objects.values( "name", "id", "course_id" ).filter( users = stundent_id )