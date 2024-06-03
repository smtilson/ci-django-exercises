from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm
#from django.http import HttpResponse

# Create your views here.
class PostList(generic.ListView):
    # this view is implicitly providing a post_list list object
    # to the template
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    `post`: An instance of :model:`blog.Post`.
    **Template:**
    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment submitted. Awaiting approval.")

    comment_form = CommentForm()
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )    

def comment_edit(request, slug, comment_id):
    '''
    View for editing a comment.
    '''
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # does this need to be specified since it likely hasn't changed??
            comment.post = post
            comment.approved = False
            comment.save()
            msg = "Comment Updated! Awaiting approval."
            messages.add_message(request, messages.SUCCESS, msg)
        else:
            msg = "Error updating comment."
            messages.add_message(request, messages.ERROR, msg)
    return HttpResponseRedirect(reverse('post_detail',args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    View for deleting comments.
    """
    queryset = Post.objects.filter(status=1)
    # this does not seem to be used anywhere.
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')
    
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
