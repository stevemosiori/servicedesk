#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'servicedesk.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# gunicorn --env DJANGO_SETTINGS_MODULE=servicedesk.settings servicedesk.wsgi --reload # Reloads as code changes
# gunicorn --env DJANGO_SETTINGS_MODULE=servicedesk.settings servicedesk.wsgi --max-requests 1 # Ensure each request starts a new worker hence all code changes are reflected. Nice on dev env