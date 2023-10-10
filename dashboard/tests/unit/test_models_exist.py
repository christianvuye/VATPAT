from django.apps import apps

def test_any_model_exists():
    my_app_config = apps.get_app_config('dashboard')
    model_dict = my_app_config.models
    assert model_dict, "No models found in the dashboard app"

