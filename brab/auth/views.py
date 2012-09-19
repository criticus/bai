from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    unregistered = True

    state = "Please log in below..."
    username = password = ''
    if request.POST:
        logout = request.POST['logout']
        if logout == 1:
            logout(request)
            return render_to_response('auth.html',{'state':state, 'username':username,'unregistered': unregistered})

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                unregistered = False
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html',{'state':state, 'username': username,'unregistered': unregistered})


