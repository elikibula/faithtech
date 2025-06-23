# home/views.py
from django.shortcuts import render
from news.models import News  # Import the News model
from shop.models import Product

def home(request):
    products = Product.objects.all()
    featured_news = News.objects.filter(is_featured=True).order_by('-date_posted')[:6]
    
    context = {
        'products': products,
        'featured_news': featured_news
    }

    return render(request, 'home/index.html', context)

    
def about_view(request):
    return render(request, 'home/about.html')