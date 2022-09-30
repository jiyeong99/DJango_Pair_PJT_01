from django.shortcuts import render, redirect
from .models import Review
from pair_pjt.settings import BASE_DIR

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews" : reviews,
    }
    return render(request, 'articles/index.html',context)

def create(request):

    title = request.GET.get('title')
    content = request.GET.get('content')
    Review.objects.create(title=title, content=content)

    context = {
        "title" : title,
        "content" : content,
    }
    return redirect('articles:index')


def new(request):

    return render(request,'articles/new.html')

def edit(request,pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review" : review,
    }
    return render(request,'articles/edit.html', context)

def update(request,pk):
    review = Review.objects.get(pk=pk)
    title = request.GET.get('title')
    content = request.GET.get('content')
    review.title = title
    review.content = content
    context = {
        "title" : title,
        "content" : content,
    }
    return render(request,'articles/edit.html')
