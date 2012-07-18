from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
    title = "PictionaryTelephone"
    description = "A project by Sam Backus to document the awesome creativity and humor of the people who play the game "
    link = "/blog/feed/"
	
    def items(self):
        return Post.objects.all().order_by("-created")[:2]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.caption
    def item_link(self, item):
         return u"/blog/%d" % item.id
	
	
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
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
	url(r'^feed', BlogFeed()),
)
