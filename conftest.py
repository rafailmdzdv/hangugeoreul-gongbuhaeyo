"""
Conftest module.

This module is used to provide
configuration, fixtures, and plugins for pytest
"""

pytest_plugins = [
    'src.tests.plugins.django_settings',
    'src.tests.plugins.days.fixtures',
]
