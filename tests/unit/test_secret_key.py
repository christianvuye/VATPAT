from django.conf import settings

def test_secret_key():
    assert hasattr(settings, 'SECRET_KEY'), "SECRET_KEY setting not found"
    assert settings.SECRET_KEY != '', "SECRET_KEY is empty"