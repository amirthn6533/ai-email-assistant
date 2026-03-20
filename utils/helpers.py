def clean_text(text):
    """
    Clean and normalize text
    """
    return text.strip()


def format_output(result):
    """
    Format the AI result nicely for printing
    """
    return f"""
📩 Email:
{result.get("text", "")}

⭐ Analysis:
{result.get("analysis", "")}

{'-' * 50}
"""


def save_to_file(content, filename="output.txt"):
    """
    Save output to a text file
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content + "\n")


def print_separator():
    """
    Print a separator line
    """
    print("=" * 50)