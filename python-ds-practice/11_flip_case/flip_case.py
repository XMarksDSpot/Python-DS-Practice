def flip_case(phrase, to_swap):
    """Swap case of occurrences of to_swap in phrase."""
    return "".join(
        char.swapcase() if char.lower() == to_swap.lower() else char for char in phrase
    )
