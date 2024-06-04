from blogging.views import (
    stub_view,
    list_view,
    detail_view,
    PostListView,
    PostDetailView,
)
from django.urls import path

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
]
