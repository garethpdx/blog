from django.template import Context, loader
from django.http import HttpResponse

from blogs.models import Post
from django.conf import settings

def go404(request):
        latest_blog_posts = blog_posts_newest_to_oldest()
        t = loader.get_template('home/404.html')
        c = Context({
                'latest_blog_posts': latest_blog_posts[:10],
                'older_blog_posts': latest_blog_posts[10:],
                'blog_config': settings.BLOG_CONFIGURATION})
        r = HttpResponse(t.render(c))
        r.status_code = 404
        return r

def index(request):
        latest_blog_posts = blog_posts_newest_to_oldest()
        t = loader.get_template('home/index.html')
        c = Context({
                'latest_blog_posts': latest_blog_posts[:10],
                'older_blog_posts': latest_blog_posts[10:],
                'blog_config': settings.BLOG_CONFIGURATION})
        return HttpResponse(t.render(c))


def blog_posts_newest_to_oldest():
    return Post.objects.filter(hidden=0).order_by('-date')
