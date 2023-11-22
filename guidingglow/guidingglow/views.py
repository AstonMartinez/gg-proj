from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': form.errors})


@login_required
def authenticate_user(request):
    user = {
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email
        # Add other user-related fields as needed
    }
    return JsonResponse(user)
