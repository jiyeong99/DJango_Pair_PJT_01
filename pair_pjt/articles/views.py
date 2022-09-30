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