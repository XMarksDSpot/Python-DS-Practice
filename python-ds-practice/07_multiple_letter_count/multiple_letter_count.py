def multiple_letter_count(phrase):
    """Return a dictionary of letter counts in phrase."""
    return {char: phrase.count(char) for char in phrase}