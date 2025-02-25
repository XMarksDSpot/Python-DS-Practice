def is_palindrome(phrase):
    """Check if phrase is a palindrome."""
    normalized = phrase.replace(" ", "").lower()
    return normalized == normalized[::-1]
