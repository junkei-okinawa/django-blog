from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment, BlogColor
from blog.forms import CommentForm


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    color = BlogColor.objects.filter(app=True).filter(theme_name="blog")[0]
    context = {
        "posts": posts,
        "color": color,
    }
    return render(request, "blog/index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    color = BlogColor.objects.filter(app=True).filter(theme_name="blog")[0]
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
        "color": color,
    }

    return render(request, "blog/detail.html", context)
