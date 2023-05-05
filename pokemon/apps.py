from django.apps import AppConfig

class PokemonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pokemon"

class TrainersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "trainers"