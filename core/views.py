from django.shortcuts import render
from .models import Post, Category
import json


def index(request):
    posts = Post.objects.all()
    content_list = [post.content for post in posts]
    content = json.loads(content_list[3])
    context = {
        "posts": posts,
        "MY_POST": content
    }
    return render(request, "theme/home_page.html", context)




# ------------------------------------
def test_view(request):
    posts = Post.objects.all()
    content_list = [post.content for post in posts]
    content = json.loads(content_list[3])
    context = {
        "posts": posts,
        "POST": content
    }
    return render(request, "theme/tv_table.html", context)
