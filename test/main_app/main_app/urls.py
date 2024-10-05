from django.contrib import admin
from django.urls import include, path

# View Import
from main_app.views import index

def login_check(func):
    def wrapper(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("로그인OO")
        else:
            print("로그인XX")
        return func(self, request, *args, **kwargs)

    return wrapper

urlpatterns = [
    path('', index, ),

    # blog app
    path('post/', include('blog.urls')),

    # account app
    path('users/', include('account.urls')),
]
