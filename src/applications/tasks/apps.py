from django.apps import AppConfig


class TasksConfig(AppConfig):
    label = 'tasks'
    name = f"applications.{label}"
