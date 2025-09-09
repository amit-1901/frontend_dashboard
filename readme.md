# Auto News Fetcher & Dashboard

## Project Description

This is a Django-based web application that automates the fetching of the latest news headlines and displays them on a simple, clean dashboard. The project demonstrates core Django concepts including models, management commands, and basic views, and includes an optional background scheduler for automated data updates.

## Features

- **Automated Data Fetching:** Fetches top headlines from a public news API.
- **Data Storage:** Stores news articles in a SQLite database using a Django `NewsArticle` model.
- **Duplicate Prevention:** Ensures that the same news article is not stored multiple times.
- **Frontend Dashboard:** Displays a list of all fetched news articles in a user-friendly table format.
- **Manual Trigger:** Provides a "Fetch Latest News" button on the UI to manually update the data.
- **Background Automation (Bonus):** Uses `django-apscheduler` to automatically fetch new headlines at regular intervals.

## Technology Stack

- **Backend:** Python, Django (4.x/5.x)
- **Database:** SQLite (default for simplicity)
- **Frontend:** HTML, Bootstrap 5
- **Dependencies:** `requests` (for API calls), `django-apscheduler` (for scheduling)

## Getting Started

### 1. Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

### 2. Installation


1. **Set up a virtual environment:** (Recommended)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

2. **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file by running `pip freeze > requirements.txt` after installing `Django`, `requests`, and `django-apscheduler`.)*

3. **Configure the News API:**
    - Get a free API key from a public news API provider (e.g., [NewsAPI.org](https://newsapi.org/)).
    - Open `news_dashboard/management/commands/fetch_news.py` and replace `'YOUR_API_KEY'` with your actual key.

### 3. Running the Application

1.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations news_dashboard
    python manage.py migrate
    ```

2.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

3.  **Access the Dashboard:**
    - Open your web browser and navigate to `http://127.0.0.1:8000/`.

You can now click the "Fetch Latest News" button to populate the dashboard with headlines.

## Manual Data Fetching

You can also run the data fetching command from the terminal at any time:
```bash
python manage.py fetch_news