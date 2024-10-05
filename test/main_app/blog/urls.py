from django.urls import path

from blog import views

urlpatterns = [
    path('add/', views.PostCreateView.as_view(), name="post-create"),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name="post-delete"),
    path('list/', views.PostListView.as_view(), name="post-list"),
    path('list/<int:pk>/',views.PostDetailView.as_view(), name="post-detail"),

    path('comment/add/',views.CommentCreateView.as_view(), name="comment-create"),
    path('comment/delete/<int:pk>', views.CommentDeleteView.as_view(), name="comment-delete"),
]