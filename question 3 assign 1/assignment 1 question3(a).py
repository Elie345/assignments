def lookup(fruit, search_term):
    """
    Looks for a key in the dictionary where the search_term is a substring (case-insensitive)
    and returns its value. Raises KeyError if nothing matches.
    """
    search_term = search_term.lower()

    for key in fruit:
        if search_term in key.lower():
            return fruit[key]

    raise KeyError(f"'{search_term}' not found in dictionary")


# Example usage
fruit = {"apple": 1, "banana": 2, "pineapple": 3}
print(lookup(fruit, "App"))  # Output: 1
print(lookup(fruit, "NANA"))  # Output: 2