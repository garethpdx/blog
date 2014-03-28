import os
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from blogs.models import Post
from blogs.models import Comment

def home(request):
    return render_to_response('home/home.html')

def index(request):
	latest_blog_posts = Post.objects.filter(hidden=0)
	t = loader.get_template('home/index.html')
	c = Context({
		'latest_blog_posts': latest_blog_posts,
		})
	return HttpResponse(t.render(c))
	
def post(request, post_id):
	post = Post.objects.get(pk=post_id)
	all_comments = Comment.objects.filter(parent_id__exact=post_id, hidden=0)
	t = loader.get_template('home/post.html')
	c = Context({'post': post, 'all_comments': all_comments})
	return HttpResponse(t.render(c))