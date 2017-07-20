from __future__ import unicode_literals

import os

from django.db import models
# from forum.models import Forum

# define the path to the document assigned in a week for a certain course
def file_location( self, file ):

  filename, file_extension = os.path.splitext( file )
  return "{0}/{1}/{2}{3}".format(self.course, self.week, filename, file_extension)


class Course( models.Model ): 

  name = models.CharField( max_length = 50 )
  code = models.CharField( max_length = 6 )
  title = models.CharField( max_length = 100 )
  desc = models.TextField()
  guide = models.FileField( upload_to = file_location )
  slug = models.SlugField( max_length = 60 )


class Week( models.Model ):
 
  name = models.CharField( max_length = 50 )
  course = models.ForeignKey( Course )
  slug = models.SlugField()


class Page( models.Model ):

  name = models.CharField( max_length = 50 )
  desc = models.TextField()
  week = models.ForeignKey( Week )
  slug = models.SlugField()