from django.shortcuts import render
from django.views import generic
from .models import Post
#from django.http import HttpResponse

# Create your views here.
class PostList(generic.ListView):
    # this view is implicitly providing a post_list list object
    # to the template
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6