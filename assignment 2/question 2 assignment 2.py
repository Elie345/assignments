# Custom exception
class IncompleteDataError(Exception):
    pass


# Generator function
def read_ledger(ledger_lines):
    for line in ledger_lines:
        if line.strip() == "":
            raise IncompleteDataError("Empty line encountered in ledger")
        yield line


# Example ledger data
ledger = [
    "Transaction A - $100",
    "Transaction B - $200",
    "",  # This will trigger the exception
    "Transaction C - $300"
]

# Calling code
if __name__ == "__main__":
    try:
        generator = read_ledger(ledger)

        for entry in generator:
            print("Processing:", entry)

    except IncompleteDataError as e:
        print("Error:", e)
        print("Safely exiting the generator loop.")