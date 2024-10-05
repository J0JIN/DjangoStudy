from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect("post/list/")
    else:
        return redirect("users/login/")