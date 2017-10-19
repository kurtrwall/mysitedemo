from django.shortcuts import render, get_object_or_404
from blog.models import Post


def index(request):
    latest_posts = Post.objects.order_by('-published_at')[:3]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})
