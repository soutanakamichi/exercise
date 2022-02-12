import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "BeEngineer_git_deploy_exercise.settings"
)

application = get_wsgi_application()
