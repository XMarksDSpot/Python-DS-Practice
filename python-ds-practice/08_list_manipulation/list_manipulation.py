def list_manipulation(lst, command, location, value=None):
    """Perform list operations based on command and location."""
    if command == "remove" and location == "end":
        return lst.pop()
    elif command == "remove" and location == "beginning":
        return lst.pop(0)
    elif command == "add" and location == "beginning":
        lst.insert(0, value)
    elif command == "add" and location == "end":
        lst.append(value)
    return lst