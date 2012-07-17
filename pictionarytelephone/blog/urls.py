from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from blog.models import Post

urlpatterns = patterns('',
    url(r'^',ListView.as_view(
                queryset=Post.objects.all().order_by("-created")[:2],
		template_name="blog.html")),
)
