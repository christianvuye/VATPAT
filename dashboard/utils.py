from datetime import datetime, timedelta

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
    Returns a list of the previous months from the current month.
    """
    today = datetime.today()
    previous_months = []
    previous_months = [(today - timedelta(days=30 * i)).strftime("%b '%y") for i in range(num_months + 1)]
    previous_months.reverse() # Reverse the list to show the oldest month first
    return previous_months