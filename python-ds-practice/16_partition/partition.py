def partition(lst, fn):
    """Partition list into two lists based on predicate function."""
    return ([item for item in lst if fn(item)], [item for item in lst if not fn(item)])