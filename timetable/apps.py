from django.apps import AppConfig

class TimetableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'timetable'

    def ready(self):
        import timetable.templatetags.custom_filters  # Register custom filters
