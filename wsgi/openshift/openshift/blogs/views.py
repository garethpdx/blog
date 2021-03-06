from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from models import Post
from models import Comment
from models import CommentForm
from django.forms import HiddenInput
from django.conf import settings

from django.core.context_processors import csrf

def home(request):
    print settings.BLOG_CONFIGURATION['site']['name']
    return render_to_response('home/home.html')


def redirect_old_url(request, post_id):
    post = Post.objects.get(pk=post_id)
    return HttpResponseRedirect('/{0.year}/{1}/{2}/'.format(post.date,
                                                            str(post.date.month).zfill(2),
                                                            post.blob))


def redirect_non_padded_url(request, post_name, post_buffered_month, post_year):
    try:
        post = Post.objects.filter(blob=post_name)[0]
    except IndexError:
        raise Post.DoesNotExist
    return HttpResponseRedirect('/{0}/{1}/{2}/'.format(post_year, post_buffered_month.zfill(2), post.blob))


def post(request, post_id=None, post_name=None, post_buffered_month=None, post_year=None, comment_redirect=False):
    try:
        if post_id:
            post = Post.objects.get(pk=post_id)
        if post_name:
            try:
                post = Post.objects.filter(blob=post_name)[0]
            except IndexError:
                raise Post.DoesNotExist
        if post.hidden:
            raise Http404
    except Post.DoesNotExist:
        raise Http404
    all_comments = Comment.objects.filter(parent_id__exact=post.pk,
                                          hidden=0)
    comment_form = CommentForm(initial={'parent': post.pk})
    comment_form.fields['parent'].widget = HiddenInput()
    latest_blog_posts = blog_posts_newest_to_oldest()
    tpl_context = Context({'post': post,
                           'all_comments': all_comments,
                           'latest_blog_posts': latest_blog_posts[:10],
                           'older_blog_posts': latest_blog_posts[10:],
                           'comment_form': comment_form,
                           'comment_redirect': comment_redirect,
                           'blog_config': settings.BLOG_CONFIGURATION,})
    tpl_context.update(csrf(request))
    return render_to_response('home/post.html', tpl_context)


def comment(request, post_id=None, post_name=None, post_buffered_month=None, post_year=None):
        if request.method == 'POST':
                f = CommentForm(request.POST)
                if f.is_valid():
                    f.save()
                    return post(request,
                                post_id=f['parent'].value(),
                                comment_redirect=True)
        form = CommentForm(request.POST)
        form.fields['parent'].widget = HiddenInput()
        return render_to_response('home/comment.html',
                                  {'form': form},
                                  context_instance=RequestContext(request))


def blog_posts_newest_to_oldest():
    return Post.objects.filter(hidden=0).order_by('-date')
