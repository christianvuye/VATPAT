from django.apps import apps

def test_dealers_model_exists():
    my_app_config = apps.get_app_config('dashboard')
    try:
        dealers_model = my_app_config.get_model('dealers')
    except LookupError:
        assert False, "No 'dealers' model found in the dashboard app"