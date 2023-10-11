from django.apps import apps

def test_creditnotes_model_exists():
    my_app_config = apps.get_app_config('dashboard')
    try:
        creditnotes_model = my_app_config.get_model('creditnotes')
    except LookupError:
        assert False, "No 'creditnotes' model found in the dashboard app"