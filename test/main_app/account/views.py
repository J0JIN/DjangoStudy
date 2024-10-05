from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from account.forms import LoginForm, SignupForm
from account.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
        
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )

            if user:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None, "사용자가 없습니다.")

        context = {
            "form" : form,
        }
        return render(request, "users/login.html", context)
    
    else:
        form = LoginForm()
        context = {
            "form" : form,
        }
        return render(request, "users/login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect("/")

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                form.add_error("password2", "비밀번호가 일치하지 않습니다")

            if User.objects.filter(username = username).exists():
                form.add_error("username", "사용중인 이름입니다")

            if form.errors:
                context = {"form" : form }
                return render(request, "users/sign_up.html", context)        
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                )
                login(request, user)
                return redirect("/")

        else:
            print("잘못된 형식")

        context = {"form" : form}
        return render(request, "users/sign_up.html", context)

    form = SignupForm()
    context = {"form" : form}
    return render(request, "users/sign_up.html", context)