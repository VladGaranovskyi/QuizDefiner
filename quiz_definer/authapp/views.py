from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .models import User
from django.contrib.auth.decorators import login_required
from quizapp.models import Quiz


def register(request):

    if request.method == 'POST':
        # getting data from the form
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # getting username and password (password1)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # creating and logging in
            user = authenticate(username=username, password=password)
            # login(request, user)
            # redirecting to login
            return redirect('/login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def my_profile(request):
    # getting data from cookies session
    quizes = Quiz.objects.only("caption", "genre").filter(author=request.user)
    return render(request, "registration/profile.html", {"user": request.user, "quizes": quizes})


def profile(request, nick):
    """
    getting data by query to the database through the nickname from the url
    """
    user = User.objects.filter(nickname=nick)[0]
    quizes = Quiz.objects.only("caption", "genre").filter(author=user)
    return render(request, "registration/profile.html", {"user": user, "quizes": quizes})
