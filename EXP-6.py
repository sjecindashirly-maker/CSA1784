def vacuum_cleaner(location, status):
    if status[location] == "Dirty":
        print("Room", location, "is Dirty.")
        print("Action: SUCK")
        status[location] = "Clean"
    else:
        print("Room", location, "is Clean.")

    if location == "A":
        print("Action: Move Right to Room B")
        location = "B"
    else:
        print("Action: Move Left to Room A")
        location = "A"

    if status[location] == "Dirty":
        print("Room", location, "is Dirty.")
        print("Action: SUCK")
        status[location] = "Clean"
    else:
        print("Room", location, "is Clean.")

    print("\nFinal Status:")
    print(status)

# Initial state
status = {
    "A": "Dirty",
    "B": "Dirty"
}

vacuum_cleaner("A", status)
