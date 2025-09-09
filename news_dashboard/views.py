# news_dashboard/views.py
from django.shortcuts import render, redirect
from django.core.management import call_command
from news_dashboard.models import NewsArticle


def dashboard(request):
    if request.method == 'POST':
        # Manually trigger the management command
        call_command('fetch_news')
        return redirect('dashboard')  # Redirect to the same page after fetching

    articles = NewsArticle.objects.all().order_by('-published_at')
    context = {
        'articles': articles
    }
    return render(request, 'news_dashboard/dashboard.html', context)