from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import CommentForm
from .models import Post, Like, Comment


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            text = request.POST.get('text')
            comment = Comment.objects.create(post=post, username=request.user, text=text)
            comment.save()
    else:
        comment_form = CommentForm()
    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'posts/detail.html', context)

def post_view(request):
    posts = Post.objects.all()
    user = request.user
    context = {'posts': posts, 'user': user}
    return render(request, 'posts/post.html', context)


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'like':
                like.value = 'unlike'
            else:
                like.value = 'like'
        like.save()
    return redirect('post')


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body', 'image']
    template_name = 'posts/create.html'
    success_url = reverse_lazy('post')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ['title', 'body', 'image']
    success_url = reverse_lazy('post')
    context_object_name = 'posts'
    login_url = 'login'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('post')
    context_object_name = 'posts'
    login_url = 'login'
