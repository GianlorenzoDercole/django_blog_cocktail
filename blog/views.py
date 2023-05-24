from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from .models import Post
from .forms import CommentForm
# Create your views here.

# get the date
def get_date(post):
    return post['date']



class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    # pass posts to index.html
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def starting_page(request):
#     # filter by date des order
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     # # sort by date
#     # sorted_posts = sorted(all_posts, key=get_date)
#     # # last 3 items
#     # latest_posts = sorted_posts[-3:]
#     return render(request, "blog/index.html", {"posts": latest_posts})



class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(request, "blog/all-posts.html", {"all_posts": all_posts})



class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context


# def post_detail(request, slug):
#     # find slug for post
#     # identified_post = next(post for post in all_posts if post['slug'] == slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {"post": identified_post, "post_tags": identified_post.tags.all() })
