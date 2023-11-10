import pyodbc
from django.conf import settings

def test_db_connection():
    db_settings = settings.DATABASES['default']
    
    connection_string = (
        f"DRIVER={{{db_settings['OPTIONS']['driver']}}};"
        f"SERVER={db_settings['HOST']};"
        f"DATABASE={db_settings['NAME']};"
        f"Trusted_Connection={db_settings['OPTIONS']['Trusted_Connection']};"
    )

    try:
        with pyodbc.connect(connection_string):
            pass
    except pyodbc.Error as e:
        assert False, f"Database connection failed! Error: {e}"