from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    name = 'portfolio'

    # TODO: Make sure this is not called twice! Or the signal connector is not called twice
    # See - http://stackoverflow.com/questions/7115097/the-right-place-to-keep-my-signals-py-files-in-django
    # See - https://docs.djangoproject.com/en/1.9/ref/applications/#methods
    def ready(self):
        pass