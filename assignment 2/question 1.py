# Function to simulate finding teammates
def find_teammates(num_needed):
    print(f"Finding {num_needed} teammate(s) to complete your team...")

# Battle Royale game mode
def battle_royale():
    num_players = int(input("Enter the number of players in your team: "))
    # Each team has 3 players
    teammates_needed = max(3 - num_players, 0)
    find_teammates(teammates_needed)
    print("Match starting . . .")

# Practice mode
def practice():
    map_name = input("Enter the desired practice map: ")
    print(f"Launching practice on {map_name}")

# Main program
def main():
    mode = input("Select game mode ('br' for Battle Royale, anything else for Practice): ").lower()
    if mode == "br":
        battle_royale()
    else:
        practice()

# Run the program
main()