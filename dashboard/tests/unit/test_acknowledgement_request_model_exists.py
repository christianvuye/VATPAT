from django.apps import apps

def test_acknowledgement_request_model_exists():
    my_app_config = apps.get_app_config('dashboard')
    try:
        acknowledgement_request_model = my_app_config.get_model('AcknowledgementRequest')
    except LookupError:
        assert False, "No 'AcknowledgementRequest' model found in the dashboard app"
