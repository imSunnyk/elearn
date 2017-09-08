from __future__ import unicode_literals

import os
import uuid

from django.db import models
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


# define the path to the guide of a course
def guide_location( self, file ):

  filename, file_extension = os.path.splitext( file )
  return "courses/{0}/{1}{2}".format(self.name, filename, file_extension)


# define the path to the document assigned in a week for a certain course
def file_location( self, file ):

  filename, file_extension = os.path.splitext( file )
  return "courses/{0}/{1}/{2}{3}".format(self.course, self.week, filename, file_extension)


class Course( models.Model ): 

  course_name = models.CharField( max_length = 50 )
  course_code = models.CharField( max_length = 6 )
  course_desc = HTMLField()
  course_guide = models.FileField( upload_to = guide_location )
  course_slug = models.SlugField( max_length = 60 )

  # override the save function
  def save( self, *args, **kwargs ):
    
    if not self.id:
      
      # Newly created object, so set slug
      self.course_slug = slugify( self.course_name )

      os.makedirs( "files/{0}/activities".format(self.course_name ) )
      os.makedirs( "files/{0}/resources".format(self.course_name ) )

    super( Course, self ).save( *args, **kwargs )

  # default display message
  def __unicode__( self ):

    return "%s" % ( self.course_name )

  # custom functions

  @classmethod
  def return_courses( self, courses_ids ) :

    courses = self.objects.all().filter( id__in = courses_ids )

    return courses


class Week( models.Model ):
 
  week_name = models.CharField( max_length = 50 )
  week_course = models.ForeignKey( Course )
  week_slug = models.SlugField()

  # override the save function
  def save( self, *args, **kwargs ):
    
    if not self.id:
      
      # Newly created object, so set slug
      self.week_slug = slugify( self.week_name )

    super( Week, self ).save( *args, **kwargs )

  # default display message
  def __unicode__( self ):

    return "%s : %s" % ( self.week_course, self.week_name )


class Book( models.Model ):

  book_name = models.CharField( max_length = 100 )
  book_week = models.ForeignKey( Week, related_name = "book_week" )
  book_slug = models.CharField( max_length = 36 )
  
  # override the save function
  def save( self, *args, **kwargs ):

    if not self.id:

      # Newly created object, so set slug
      self.book_slug = str( uuid.uuid4() ).replace( "-" , "") 

      super( Book, self ).save( *args, **kwargs )
  
  # default display message
  def __unicode__( self ):

    return "%s : %s" % ( self.book_week, self.book_name )


class Subchapter( models.Model ) :

  subch_name = models.CharField( max_length = 100 )
  subch_book = models.ForeignKey( Book, related_name = "subch_book" )
  subch_slug = models.CharField( max_length = 36 )

  # override the save function
  def save( self, *args, **kwargs ):

    if not self.id:

      # Newly created object, so set slug
      self.subchslug = str( uuid.uuid4() ).replace( "-" , "") 

      super( Subchapter, self ).save( *args, **kwargs )

  # default display message
  def __unicode__( self ):

    return "%s : %s" % ( self.subch_book, self.subch_name )

class Page( models.Model ):

  page_name = models.CharField( max_length = 100 )
  page_desc = models.TextField()
  page_book = models.ForeignKey( Book, related_name = "page_book", blank = True, null = True )
  page_subch = models.ForeignKey( Subchapter, related_name = "page_subch", blank = True, null = True )
  page_slug = models.SlugField()

  # override the save function
  def save( self, *args, **kwargs ):
    
    if not self.id:
      
      # Newly created object, so set slug
      self.page_slug = slugify( self.page_name )

    super( Page, self ).save( *args, **kwargs )

  # default display message
  def __unicode__( self ):

    if self.page_subch is not None : 

      return " %s : %s " % ( self.page_subch, self.page_name )

    else : 

      return "%s : %s " % ( self.page_book, self.page_name )
