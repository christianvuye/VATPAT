from django.db import connections
from django.db.utils import OperationalError

def test_db_connection():
    db_conn = connections['default']
    try:
        db_conn.connect()
    except OperationalError:
        assert False, "Database connection failed!"
    else:
        assert True
    finally:
        db_conn.close()