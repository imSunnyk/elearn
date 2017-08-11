import os

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from resources.models import Resource 

@login_required
def resource( request, resource_slug ):
	# get the file

	res = Resource.objects.all().get( slug = resource_slug )

	file = res.document_path

	base = os.path.basename( file.path )
	file_name = os.path.splitext( base )

    # get the file data
	data = open( file.path, "r" )
    
    # download 
	response = HttpResponse( data.read() , content_type='application/vnd')
	response[ 'Content-Length' ] = os.path.getsize( file.path )
	response['Content-Disposition'] = 'inline;filename=some_file.pdf' 

	return response
