from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout


def admin_login_view(request, *args, **kwargs):
    user = request.user
    if request.method == "GET":
        form = LoginForm()
        context = {
            'login_form': form,
        }
        return render(request, 'customadmin/login.html', context)

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user.is_superuser:
                login(request, user)
                return render(request, 'customadmin/dashboard.html')
    else:
        form = LoginForm()
    context = {"login_form": form}
    return render(request, 'customadmin/login.html', context)


def logout_view(request):
    logout(request)
    return redirect("adminlogin")
