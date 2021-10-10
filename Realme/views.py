from django.shortcuts import render
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


# Create your views here.
def home(request):
    template_name='Realme/index.html'
    return render(request, template_name)


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'Resume_Tushar Kshirsagar_Software Engineer.pdf'
    # Define the full file path
    filepath = BASE_DIR + '/Realme/static/images' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response