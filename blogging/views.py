from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from blogging.models import Post

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    model = Post
    template_name = "blogging/list.html"
    # Exclude posts that have not been published yet and order by published date
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        for arg in args:
            body += f"    {arg}\n"
    if kwargs:
        body += "Kwargs:\n"
        for key, value in kwargs.items():
            body += f"    {key}: {value}\n"
    return HttpResponse(body, content_type="text/plain")


def old_list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by("-published_date")
    template = loader.get_template("blogging/list.html")
    context = {"posts": posts}
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by("-published_date")
    context = {"posts": posts}
    return render(request, "blogging/list.html", context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {"post": post}
    return render(request, "blogging/detail.html", context)
