from datetime import datetime


def get_current_date():
    return datetime.now().strftime('%A, %B %d, %Y')
