import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from resources.models import Resource 

@login_required
def resource( request, resource_slug ):
	# get the file

	my_res = Resource.objects.all().get( resource_slug = resource_slug )

	my_file = my_res.resource_document_path

	my_base = os.path.basename( my_file.path )
	my_file_name = os.path.splitext( my_base )

    # get the file data
	my_data = open( my_file.path, "r" )
    
    # download 
	response = HttpResponse( my_data.read() , content_type='application/vnd')
	response[ 'Content-Length' ] = os.path.getsize( my_file.path )
	response['Content-Disposition'] = 'inline;filename=some_file.pdf' 

	return response
