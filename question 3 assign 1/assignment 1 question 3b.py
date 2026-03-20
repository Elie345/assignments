def lookup(fruit, search_term):
    """
    Looks for a key in the dictionary where the search_term is a substring (case-insensitive).

    Returns:
        tuple: (matching_key, value)

    Raises:
        KeyError: If no matches or multiple matches are found
    """
    search_term = search_term.strip().lower()  # ignore extra spaces and make lowercase
    matches = []

    for key in fruit:
        if search_term in key.lower():
            matches.append((key, fruit[key]))

    if len(matches) == 0:
        raise KeyError("search term not found")
    elif len(matches) > 1:
        raise KeyError("multiple keys found")
    else:
        return matches[0]


# ------------------ TEST ------------------
fruit = {"apple": 1, "banana": 2, "pineapple": 3}

# Use try-except to safely handle KeyErrors
test_terms = ["app", "nana", "berry", "Apple", " pine "]

for term in test_terms:
    try:
        result = lookup(fruit, term)
        print(f"Search '{term}' -> Found: {result}")
    except KeyError as e:
        print(f"Search '{term}' -> Error: {e}")