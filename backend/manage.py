#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acd_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Vérifiez votre installation et que "
            "DJANGO_SETTINGS_MODULE est bien défini."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
