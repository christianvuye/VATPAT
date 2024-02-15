from django.apps import apps

def test_any_model_exists():
    my_app_config = apps.get_app_config('dashboard')
    # Model_dict to check for any models in app, get_model is for specific models.
    model_dict = my_app_config.models
    assert model_dict, "No models found in the dashboard app"

