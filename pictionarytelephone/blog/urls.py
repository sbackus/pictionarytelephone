from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = patterns('blog.views',
    url(r'^$',ListView.as_view(
                queryset=Post.objects.all().order_by("-created")[:2],
		template_name="blog.html")),
    url(r'^(?P<pk>\d+)',DetailView.as_view(
                model = Post,
		template_name="post.html")),
    url(r'^archives',ListView.as_view(
                queryset=Post.objects.all().order_by("-created"),
		template_name="archives.html")),	
		
		
)
