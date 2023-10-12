from django.apps import apps

def test_acknowledgement_received_model_exists():
    my_app_config = apps.get_app_config('dashboard')
    try:
        acknowledgement_received_model = my_app_config.get_model('AcknowledgementReceived')
    except LookupError:
        assert False, "No 'AcknowledgementReceived' model found in the dashboard app"
