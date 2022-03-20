#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# import dotenv


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelPj.settings')
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
    # dotenv.read_dotenv() # .env파일을 읽도록, 여기에는 암호화/복호화 알고리즘과 비밀키를 넣어줌.
    main()
