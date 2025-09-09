# news_dashboard/apps.py
from django.apps import AppConfig

class NewsDashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_dashboard'

    def ready(self):
        from . import scheduler
        scheduler.start()