from blogging.views import stub_view, list_view, detail_view
from django.urls import path

urlpatterns = [
    path("", list_view, name="blog_index"),
    path("posts/<int:post_id>/", detail_view, name="blog_detail"),
]
