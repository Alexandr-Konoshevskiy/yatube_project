from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Create your views here.

def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    title = "Это главная страница проекта Yatube"
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts_list/'
    title = "Здесь будет информация о группах проекта Yatube"
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
