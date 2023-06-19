from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from pokedex.models import Team


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        # serve the login page
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        # create the user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save the user
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('home')
    else:
        # serve the registration page
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required(login_url='/users/login/')
def profile_view(request):
    
    team = Team.objects.all()
    
    context = {
        'teams': team
    }
    
    
    
    return render(request, 'users/profile.html', context)

@login_required(login_url='/users/login/')
def team(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    context = {
        "team": team
    }
    return render(request, 'pokedex/teams.html', context)

