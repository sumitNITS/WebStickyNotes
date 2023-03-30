import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sticky_Notes.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django import Failed! Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Is your "
            "virtual environment active?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
