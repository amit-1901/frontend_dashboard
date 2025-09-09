# news_dashboard/management/commands/fetch_news.py
import requests
from django.core.management.base import BaseCommand
from news_dashboard.models import NewsArticle
from datetime import datetime


class Command(BaseCommand):
    help = 'Fetches the latest news headlines and saves them to the database.'

    def handle(self, *args, **options):
        # Using a public RSS feed as an example, e.g., BBC News Top Stories
        # You would need to parse the XML response.
        # This example uses a simplified API endpoint for demonstration.
        api_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=eac6a04a27b84278a0c910e2ec82013f'  # Replace with your API key

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            new_articles_count = 0
            for article in data['articles']:
                title = article.get('title')
                published_at_str = article.get('publishedAt')

                # Check for required fields
                if not title or not published_at_str:
                    continue

                # Check for duplicates based on title
                if NewsArticle.objects.filter(title=title).exists():
                    continue

                # Create and save a new article
                NewsArticle.objects.create(
                    title=title,
                    summary=article.get('description', ''),
                    source=article.get('source', {}).get('name', 'Unknown'),
                    published_at=datetime.strptime(published_at_str, '%Y-%m-%dT%H:%M:%SZ')
                )
                new_articles_count += 1

            self.stdout.write(self.style.SUCCESS(f'Successfully fetched and saved {new_articles_count} new articles.'))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching news: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unexpected error occurred: {e}'))