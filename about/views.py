from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse
from django.conf import settings
import os


# Create your views here.


def about(request):
    user_profile = UserProfile.objects.first()

    return render(request, 'about.html', {'user_profile': user_profile})


def download_cv(request):
    # Define the path to the file
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv', 'Rinshad_CV.pdf')
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file and create a response object
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Rinshad_CV.pdf"'
            return response
    
    # Return a 404 error if the file does not exist
    return HttpResponse("File not found", status=404)

