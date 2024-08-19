from .models import UserProfile

def user_profile(request):
    return {
        'user_profile': UserProfile.objects.first(),
    }
