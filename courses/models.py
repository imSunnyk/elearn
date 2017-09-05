from __future__ import unicode_literals

import os

from django.db import models
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


# define the path to the guide of a course
def guide_location( self, file ):

  filename, file_extension = os.path.splitext( file )
  return "{0}/{1}{2}".format(self.name, filename, file_extension)


# define the path to the document assigned in a week for a certain course
def file_location( self, file ):

  filename, file_extension = os.path.splitext( file )
  return "{0}/{1}/{2}{3}".format(self.course, self.week, filename, file_extension)


class Course( models.Model ): 

  name = models.CharField( max_length = 50 )
  code = models.CharField( max_length = 6 )
  desc = HTMLField()
  guide = models.FileField( upload_to = guide_location )
  slug = models.SlugField( max_length = 60 )

  # override the save function
  def save( self, *args, **kwargs ):
    
    if not self.id:
      
      # Newly created object, so set slug
      self.slug = slugify( self.name )

      os.makedirs( "files/{0}/activities".format(self.name ) )
      os.makedirs( "files/{0}/resources".format(self.name ) )

    super( Course, self ).save( *args, **kwargs )

  # default display message
  def __unicode__( self ):

    return "%s" % ( self.name )

  # custom functions

  @classmethod
  def return_courses( self, courses_ids ) :

    courses = self.objects.all().filter( id__in = courses_ids )

    return courses


class Week( models.Model ):
 
  name = models.CharField( max_length = 50 )
  course = models.ForeignKey( Course )
  slug = models.SlugField()

  # override the save function
  def save( self, *args, **kwargs ):
    
    if not self.id:
      
      # Newly created object, so set slug
      self.slug = slugify( self.name )

    super( Week, self ).save( *args, **kwargs )

  # default display message
  def __unicode__( self ):

    return "%s : %s" % ( self.course, self.name )


class Page( models.Model ):

  name = models.CharField( max_length = 50 )
  desc = models.TextField()
  week = models.ForeignKey( Week )
  slug = models.SlugField()

  # override the save function
  def save( self, *args, **kwargs ):
    
    if not self.id:
      
      # Newly created object, so set slug
      self.slug = slugify( self.name )

    super( Page, self ).save( *args, **kwargs )

  # default display message
  def __unicode__( self ):

    return "%s : %s" % ( self.week, self.name )