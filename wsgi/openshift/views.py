from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from blogs.models import Post
from blogs.models import Comment
from blogs.models import CommentForm


def home(request):
    return render_to_response('home/home.html')


def go404(request):
        latest_blog_posts = Post.objects.filter(hidden=0)
        t = loader.get_template('home/404.html')
        c = Context({
            'latest_blog_posts': latest_blog_posts[:10],
            'older_blog_posts': latest_blog_posts[10:]})
        r = HttpResponse(t.render(c))
        r.status_code = 404
        return r


def index(request):
        latest_blog_posts = Post.objects.filter(hidden=0)
        t = loader.get_template('home/index.html')
        c = Context({
            'latest_blog_posts': latest_blog_posts[:10],
            'older_blog_posts': latest_blog_posts[10:]})
        return HttpResponse(t.render(c))


def redirect_old_url(request, post_id):
    post = Post.objects.get(pk=post_id)
    return HttpResponseRedirect('/{0.year}/{0.month}/{1}/'.format(post.date,
                                                                  post.blob))


def post(request, post_id=None, post_name=None):
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
    #  t = loader.get_template('home/post.html')
    c = Context({'post': post, 'all_comments': all_comments,
                 'comment_form': CommentForm()})
    return render_to_response('home/post.html',
                              c,
                              context_instance=RequestContext(request))


def comment(request, post_name=None):
        if request.method == 'POST':
                f = CommentForm(request.POST)
                if f.is_valid():
                    new_comment = f.save(commit=False)
                    parent = Post.objects.filter(blob=post_name)[0]
                    new_comment.parent_id = parent.id
                    new_comment.save()
                #else:
                #    print f
                return HttpResponseRedirect('/{0.year}/{0.month}/{1}/'.format(parent.date, 
                                                                              parent.blob))
        form = CommentForm()
        return render_to_response('home/comment.html',
                                  {'form': form},
                                  context_instance=RequestContext(request))
