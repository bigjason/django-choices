import django


def has_new_migrations():
    return (django.VERSION[:2] >= (1, 7), "Test requires the Django migrations introduced in Django 1.7")
