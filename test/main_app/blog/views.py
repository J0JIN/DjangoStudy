from typing import Any
from django.db.models.base import Model as Model
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from blog.forms import CommentForm, PostForm
from blog.models import Post, Comment
from django.views import generic

# Post View
class PostDeleteView(generic.DeleteView):
    model = Post
    form_class = PostForm
    success_url = "/post/list"

class PostListView(generic.ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post/post_list.html"
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post/post_detail.html"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm
        return context
    
class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    success_url = "/post/list"

    def get(self, request: HttpRequest, *args: str, **kwargs: Any):
        self.template_name = "post/post_add.html"
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse('post-list')
    

# Comment View
class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.request.POST.get('post')})

class CommentDeleteView(generic.DeleteView):
    model = Comment
    form_class = CommentForm

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        post_id = Comment.objects.get(id = self.object.pk).post.pk
        success_url = self.get_success_url(post_id)
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_success_url(self, post_id):
        return reverse('post-detail', kwargs={'pk': post_id})

