from .models import CreditNotes
from .utils import get_previous_month_date_range
from collections import defaultdict

def collect_credit_notes_from_previous_month():
    """
    Collect all credit notes from the previous month.
    """
    start_date, end_date = get_previous_month_date_range()
    credit_notes = CreditNotes.objects.filter(IssuedDate__range=[start_date, end_date])
    
    return credit_notes

def collect_credit_notes_from_previous_month_grouped_by_dealer():
    """
    Collect all credit notes from the previous month and group them by dealer.
    """
    credit_notes = collect_credit_notes_from_previous_month()

    grouped_credit_notes = defaultdict(list)
    for note in credit_notes:
        grouped_credit_notes[note.D_ID.DealerName].append(note)
    
    return grouped_credit_notes