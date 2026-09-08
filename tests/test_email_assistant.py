import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
﻿from utils.helpers import clean_text, format_output
from gmail.gmail_reader import get_emails

def test_clean_text():
    raw = "   Important update for tomorrow!   \n"
    assert clean_text(raw) == "Important update for tomorrow!"

def test_get_emails():
    emails = get_emails()
    assert isinstance(emails, list)
    assert len(emails) > 0

def test_format_output():
    sample = {"text": "Test email", "analysis": "High priority"}
    formatted = format_output(sample)
    assert "Test email" in formatted
    assert "High priority" in formatted
