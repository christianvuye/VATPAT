from .models import CreditNotes
from .utils import get_previous_month_date_range

def collect_credit_notes_from_previous_month():
    """
    Collect all credit notes from the previous month.
    """
    start_date, end_date = get_previous_month_date_range()
    credit_notes = CreditNotes.objects.filter(IssuedDate__range=[start_date, end_date])
    
    return credit_notes