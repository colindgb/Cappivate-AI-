import datetime

def get_current_timestamp():
    return datetime.datetime.now().isoformat()

def format_text(text):
    return text.strip().capitalize()
