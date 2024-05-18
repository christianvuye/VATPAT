from .models import CreditNotes
from .utils import get_previous_month_date_range
# from collections import defaultdict

def collect_credit_notes_from_previous_month():
    """
    Collect all credit notes from the previous month.
    """
    start_date, end_date = get_previous_month_date_range()
    credit_notes = CreditNotes.objects.filter(IssuedDate__range=[start_date, end_date])
    
    return credit_notes # returns a QuerySet

def collect_unique_dealers_from_credit_notes(credit_notes):
    """
    Collect all unique dealers from a credit_notes queryset.
    """
    #credit_notes = collect_credit_notes_from_previous_month() # returns a QuerySet

    # define empty list
    unique_dealer_list = []

    # iterate through the QuerySet
    for note in credit_notes: 
        if note.D_ID.DealerName not in unique_dealer_list:
            unique_dealer_list.append(note.D_ID.DealerName)
    
    return unique_dealer_list

def credit_notes_previous_month_per_dealer_dict(credit_notes, unique_dealer_list):
    """
    Create a dictionary with dealers as keys and their credit notes as values.
    """
    # Group credit notes by dealer, don't use defaultdict
    grouped_credit_notes = {}

    for dealer in unique_dealer_list:
        grouped_credit_notes[dealer] = []
        for note in credit_notes:
            if note.D_ID.DealerName == dealer:
                grouped_credit_notes[dealer].append(note)
    
    return grouped_credit_notes