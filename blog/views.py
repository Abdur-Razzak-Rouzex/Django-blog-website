from django.shortcuts import render


posts = [
    {
        'title': 'post 1',
        'author': 'A Razzak',
        'content': 'This is the first post of the blog',
        'date_posted': '20 jan, 2020'
    },
    {
        'title': 'post 2',
        'author': 'A Rouzex',
        'content': 'This is the post you want to see, as a second post',
        'date_posted': '10 jan, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})