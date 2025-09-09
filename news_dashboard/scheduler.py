# news_dashboard/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command

def start():
    scheduler = BackgroundScheduler()
    # Schedule the fetch_news command to run every 60 minutes
    scheduler.add_job(lambda: call_command('fetch_news'), 'interval', minutes=60)
    scheduler.start()