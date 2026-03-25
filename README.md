# Delivery Tracker

A Django web application for tracking deliveries.

## Setup

1. Ensure Python 3.10+ is installed.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Apply database migrations:
   ```
   python manage.py migrate
   ```
4. Run the development server:
   ```
   python manage.py runserver
   ```
5. Open your browser to `http://127.0.0.1:8000/`

## Project Structure

- `manage.py`: Django's command-line utility.
- `deliverytracker/`: Project settings and configuration.
  - `settings.py`: Main settings file.
  - `urls.py`: URL routing.
  - `wsgi.py`: WSGI configuration for deployment.
- `pages/`: App for static pages.
  - `templates/pages/`: HTML templates.
  - `views.py`: View functions.
  - `urls.py`: App URL routing.
- `tracker/`: App for delivery tracking with CRUD operations.
  - `models.py`: WeeklyDelivery model with start_date and end_date fields
  - `templates/tracker/`: HTML templates for CRUD with date inputs
  - `views.py`: Class-based views for list, create, update, delete.
  - `urls.py`: App URL routing.

## Available Pages

- **Home** (`/`): Welcome page with basic information about the delivery tracker.
- **Delivery Tracker** (`/tracker/`): Weekly internal delivery table with CRUD operations.
  - View all entries in a formatted table
  - Add new entries with unrestricted calendar date picker
  - Edit existing entries with auto-calculating week ranges
  - Delete entries
  - View totals across all weeks

## Admin Interface

- **Admin Panel** (`/admin/`): Django admin interface (login: admin/admin)

## Next Steps

- Create Django apps for specific features (e.g., `python manage.py startapp tracker`)
- Configure database in `settings.py`
- Add models, views, and templates as needed.
- Customize the HTML templates in `pages/templates/pages/` and `tracker/templates/tracker/`

## Troubleshooting

- If `django-admin` is not recognized, use `python -m django` instead.
- Ensure virtual environment is activated if using one.