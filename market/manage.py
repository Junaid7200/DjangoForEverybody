#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():

    # Special PythonAnywhere check to mention not to use runserver
    pythonanywhere = os.getenv('PYTHONANYWHERE_DOMAIN')
    if pythonanywhere is not None and 'runserver' in sys.argv :
        print('')
        print('*********')
        print('You should not use "runserver" on PythonAnywhere - use ')
        print('   python manage.py check')
        print('and reload your application under the Web tab or in the file editor')
        print('*********')
        quit()
    # End of PythonAnywhere check

    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
