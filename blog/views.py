from django.shortcuts import render

from datetime import date
# Create your views here.





















all_posts = [
    {
        "slug": "iuyoiuyoiuyoi",
        "image": "chillies.png",
        "author": "oiuyoiuy",
        "date": date(2022, 7, 21),
        "title": "mountian",
        "excerpt": "iuyoiuyoiuyoiu",
        "content": 'oiuyoiuyoiuyiouyoiuyioyu'
    },
        {
        "slug": "iuyoiuyoiuyoi",
        "image": "chillies.png",
        "author": "oiuyoiuy",
        "date": date(2022, 8, 21),
        "title": "opiupouipoiu",
        "excerpt": "iuyoiuyoiuyoiu",
        "content": 'oiuyoiuyoiuyiouyoiuyioyu'
    },
        {
        "slug": "iuyoiuyoiuyoi",
        "image": "chillies.png",
        "author": "oiuyoiuy",
        "date": date(2022, 9, 21),
        "title": "gbvbvbvbvbvbv",
        "excerpt": "iuyoiuyoiuyoiu",
        "content": 'oiuyoiuyoiuyiouyoiuyioyu'
    }
]

# get the date
def get_date(post):
    return post['date']

def starting_page(request):
    # sort by date
    sorted_posts = sorted(all_posts, key=get_date)
    # last 3 items
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})

def post_detail(request, slug):
    # find slug for post
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
