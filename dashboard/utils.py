from datetime import datetime, timedelta

"""
You could make these functions more generic. But only write code you actually need.

Only make a specific function more generic if you need that generic functionality in multiple places.

This file seems fine, no comments.
"""
def get_previous_month_date_range(): 
    """
    Returns the first and last day of the previous month.
    """
    today = datetime.today()
    first_day_current_month = today.replace(day=1)
    last_day_previous_month = first_day_current_month - timedelta(days=1)
    first_day_previous_month = last_day_previous_month.replace(day=1)
    return first_day_previous_month, last_day_previous_month

def get_previous_months(num_months):
    """
    Returns a list of the previous months from the current month, including the current month.
    """
    current_date = datetime.now()
    previous_months = [current_date.strftime("%B '%y")]

    for i in range(num_months - 1):
        previous_month_date = current_date.replace(day=1) - timedelta(days=1)
        previous_month = previous_month_date.strftime("%B '%y")
        previous_months.append(previous_month)
        current_date = previous_month_date

    return previous_months