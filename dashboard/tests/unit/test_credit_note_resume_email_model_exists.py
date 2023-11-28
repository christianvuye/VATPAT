from django.apps import apps

def test_credit_note_resume_email_model_exists():
    my_app_config = apps.get_app_config('dashboard')
    try:
        my_app_config.get_model('CreditNoteResumeEmail')
    except LookupError:
        assert False, "No 'CreditNoteResumeEmail' model found in the dashboard app"
