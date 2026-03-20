from gmail.gmail_reader import get_emails
from ai.analyzer import analyze_email
from utils.helpers import format_output, save_to_file
from database.db import init_db, save_email
emails = get_emails()
init_db()
for email in emails:
    result = analyze_email(email)
    save_email(result["text"], result["analysis"])
    output = format_output(result)

    print(output)
    save_to_file(output)