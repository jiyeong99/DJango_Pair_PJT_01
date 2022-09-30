from multiprocessing import context
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

def detail(request,pkk):
    review = Review.objects.get(pk = pkk)
    context = {
        'review' : review,
    }
    return render(request, 'articles/detail.html', context)

def edit(request,pkk):
    review = Review.objects.get(pk=pkk)
    context = {
        "review":review,
    }
    return render(request,'articles/edit.html',context)

def update(request,pkk):
    review = Review.objects.get(pk=pkk)

    u_title = request.GET.get('title')
    u_content = request.GET.get('content')

    review.title = u_title
    review.content = u_content
    review.save()

    return redirect('articles:detail', review.pk)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('articles:index')


